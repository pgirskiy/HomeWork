import hw7.bookscreator as bcr
import unittest


class TestBookCreate(unittest.TestCase):

    def setUp(self) -> None:
        self.my_book = bcr.PyBook('test title1', 'test author1')
        self.create_code, self.create_resp = self.my_book.book_create()

    def tearDown(self) -> None:
        self.my_book.book_del()

    def testCreateStatusCode(self):
        self.assertEqual(self.create_code, 201)

    def testCreateResp(self):
        v_dic = {'id': self.my_book.book_id, 'title': self.my_book.title, 'author': self.my_book.author}
        self.assertCountEqual(self.create_resp, v_dic)

    def testBookCheckWithGet(self):
        a = self.my_book.check_book(self.my_book.book_url)
        self.assertTrue(a)

    def testFullListBookCheck(self):
        a = self.my_book.find_my_data()
        self.assertTrue(a)

    def testBookUpdate(self):
        code, resp = self.my_book.book_edit('TestTitle2', 'TestAuthor2')
        v_dic = {'id': self.my_book.book_id, 'title': self.my_book.title, 'author': self.my_book.author}
        c = self.my_book.find_my_data()
        self.assertEqual(code, 200)
        self.assertCountEqual(resp, v_dic)
        self.assertTrue(c)

    def testBookUpdateEmptyData(self):
        code, resp = self.my_book.book_edit('', '')
        self.assertEqual(code, 400)
        self.assertEqual(resp['title'], ['This field may not be blank.'])
        self.assertEqual(resp['author'], ['This field may not be blank.'])

    def testBookUpdateLongData(self):
        code, resp = self.my_book.book_edit('t' * 100, 'a' * 100)
        self.assertEqual(code, 400)
        self.assertEqual(resp['title'], ['Ensure this field has no more than 50 characters.'])
        self.assertEqual(resp['author'], ['Ensure this field has no more than 50 characters.'])


class TestBookDel(unittest.TestCase):

    def testBookDelCode(self):
        self.my_book = bcr.PyBook('test title1', 'test author1')
        self.my_book.book_create()
        code = self.my_book.book_del()
        self.assertEqual(code, 204)

    def testDelAnyBook(self):
        self.my_book = bcr.PyBook()
        self.my_book.book_url = "http://pulse-rest-testing.herokuapp.com/books/0/"
        code = self.my_book.book_del()
        self.assertEqual(code, 404)


class TestRoleCreate(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.my_book = bcr.PyBook('My_title1', 'My_author1')
        a, b = cls.my_book.book_create()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.my_book.book_del()

    def setUp(self) -> None:
        self.my_role = bcr.PyRole(self.my_book.title, self.my_book.author, 'teacher', 'NoType', 80)

    def tearDown(self) -> None:
        self.my_role.all_role_del()

    def testOneRoleCreate(self):
        self.role_code, self.role_resp = self.my_role.role_create(self.my_book.book_url, self.my_role.role_name,
                                                                  self.my_role.role_type, self.my_role.role_level)
        self.assertEqual(self.role_code, 201)

    def testManyRolesTest(self):
        role_list = [['rol-1', 'type-1', 1],
                     ['rol-2', 'type-2', 2],
                     ['rol-3', 'type-3', 3]]
        for role in role_list:
            with self.subTest(role):
                self.role_code, self.role_resp = self.my_role.role_create(self.my_book.book_url, *role)
                self.assertEqual(self.role_code, 201)

        c_role_url = self.my_role.role_url.copy()

        for role in c_role_url.keys():
            with self.subTest(role):
                del_code = self.my_role.role_del(role)
                self.assertEqual(del_code, 204)

    def testRoleCheckWithGet(self):
        self.role_code, self.role_resp = self.my_role.role_create(self.my_book.book_url, self.my_role.role_name,
                                                                  self.my_role.role_type, self.my_role.role_level)
        for item in self.my_role.role_url.values():
            with self.subTest(item):
                a = self.my_role.check_book(item)
                self.assertTrue(a)


if __name__ == '__main()':
    unittest.main()
