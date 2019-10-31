import hw7.bookscreator as bcr
import pytest


@pytest.fixture(scope='session')
def tutorial():
    return bcr.PyBook('test title1', 'test author1')


@pytest.fixture(scope='session')
def book_create(tutorial):
    create_code, create_resp = tutorial.book_create()
    yield [create_code, create_resp]
    if tutorial.book_url: tutorial.book_del()


@pytest.fixture(scope='session')
def my_role(tutorial):
    return bcr.PyRole(tutorial.title, tutorial.author, 'teacher1', 'Type1', 80)


@pytest.fixture(scope='session')
def role_create(tutorial, my_role):
    code, resp = my_role.role_create(tutorial.book_url, my_role.role_name, my_role.role_type, my_role.role_level)
    yield [code, resp]
    my_role.all_role_del()


def test_book_create_code(tutorial, book_create):
    assert book_create[0] == 201


def test_book_create_resp(tutorial, book_create):
    assert book_create[1]['title'] == tutorial.title and book_create[1]['author'] == tutorial.author


def test_book_get_check(tutorial):
    a = tutorial.check_book(tutorial.book_url)
    assert a is True


def test_book_in_full_list(tutorial):
    a = tutorial.find_my_data()
    assert a is True


@pytest.mark.parametrize('title, author', [('test title2', 'test author2'), ('test title3', 'test author3')],
                         ids=['Update Book Data 1', 'Update Book Data 2'])
def test_book_update(tutorial, title, author):
    code, resp = tutorial.book_edit(title, author)
    assert code == 200
    assert resp['title'] == tutorial.title and resp['author'] == tutorial.author
    assert tutorial.find_my_data() is True


def test_book_upd_empty(tutorial):
    code, resp = tutorial.book_edit('', '')
    assert code == 400
    assert resp['title'] == ['This field may not be blank.']
    assert resp['author'] == ['This field may not be blank.']


def test_book_upd_long(tutorial):
    code, resp = tutorial.book_edit('t' * 100, 'a' * 100)
    assert code == 400
    assert resp['title'] == ['Ensure this field has no more than 50 characters.']
    assert resp['title'] == ['Ensure this field has no more than 50 characters.']


def test_book_delete(tutorial):
    assert tutorial.check_book(tutorial.book_url)
    code = tutorial.book_del()
    assert code == 204


def test_bad_book_del(tutorial):
    tutorial.book_url = "http://pulse-rest-testing.herokuapp.com/books/0/"
    code = tutorial.book_del()
    assert code == 404


def test_role_create(role_create, my_role):
    assert role_create[0] == 201
    assert role_create[1]['name'] == my_role.role_name
    assert role_create[1]['type'] == my_role.role_type
    assert role_create[1]['level'] == my_role.role_level


@pytest.mark.parametrize('name, rtype, level', [('rol-1', 'type-1', 1),
                                                ('rol-2', 'type-2', 2),
                                                ('rol-3', 'type-3', 3)],
                         ids=['Create Role 1', 'Create Role 2', 'Create Role 3'])
def test_role_create_list(my_role, tutorial, name, rtype, level):
    code, resp = my_role.role_create(tutorial.book_url, name, rtype, level)
    assert code == 201


def test_role_delete_list(my_role):
    c_role_url = my_role.role_url.copy()
    for role in c_role_url.keys():
        code = my_role.role_del(role)
        assert code == 204
