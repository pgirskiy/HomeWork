import requests
import json

#модуль из домашнего задания 6
#Закоментированны проверки и строчки которые помешают тесту в домашнем задании

class PyBook:
    """book obj for rest api homework 6"""
    a_url = "http://pulse-rest-testing.herokuapp.com/books/"
    b_url = "http://pulse-rest-testing.herokuapp.com/roles/"

    def __init__(self, title: str = None, author: str = None):
        self.title = title
        self.author = author
        self.book_id = None
        self.book_url = None
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        #self.book_create()

    def __str__(self):
        return f'Book {self.title}, {self.author},  ID {self.book_id}, URL {self.book_url}'

    def check_book(self, url, code=200):
        """
        :param url: get url for check
        :param code: response code
        "check url with get request
        """
        if requests.get(url, timeout=5).status_code == code:
            return True

    def find_my_data(self):
        """Verified book on server"""
        resp_all = requests.get(self.a_url, timeout=5).json()
        try:
            for val in resp_all:
                if val['title'] == self.title and val['author'] == self.author:
                    return True
        except IndexError:
            return False

    def book_create(self):
        """creates a book, save id and link.
        Verifies that the book exists"""
        if self.check_book(self.a_url) and self.title and self.author:
            book_js = json.dumps({'title': self.title, 'author': self.author})
            post_resp1 = requests.post(self.a_url, data=book_js, headers=self.headers)
            #assert post_resp1.status_code == 201, f"Books create error {post_resp1.json()}"
            self.book_id = post_resp1.json()['id']
            self.book_url = self.a_url + str(self.book_id)
            #assert self.find_my_data(), 'The book does not exist on the server'
            return post_resp1.status_code, post_resp1.json()

    def book_edit(self, title: str, author: str):
        """book edit, get new title and author"""
        if self.check_book(self.book_url):
            book_js = json.dumps({'title': title, 'author': author})
            put_resp1 = requests.put(self.book_url, data=book_js, headers=self.headers)
            #assert put_resp1.status_code == 200, "Book edit error"
            self.title = title
            self.author = author
            #assert self.find_my_data(), 'The book does not exist on the server'
            return put_resp1.status_code, put_resp1.json()

    def book_del(self):
        """delete book"""
        #if self.check_book(self.book_url):
        del_resp1 = requests.delete(self.book_url)
        #assert del_resp1.status_code == 204, "Books delete error"
        self.book_id = None
        self.book_url = None
        return del_resp1.status_code


class PyRole(PyBook):
    """role for book"""

    def __init__(self, title, author, role_name, role_type, role_level):
        self.role_url = {}
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.role_name = role_name
        self.role_type = role_type
        self.role_level = role_level
        #self.role_create(self.role_name, self.role_type, self.role_level)

    def __str__(self):
        return f'Book {self.book_id}, Role {self.role_name}, ID {self.role_url.keys()}, URL {self.role_url.values()}'

    def role_create(self, book_url, role_name, role_type, role_level):
        """creates a role, save id and link.
        Verifies that the role exists"""
        if self.check_book(self.b_url):
            role_js = json.dumps({'name': role_name, 'type': role_type,
                                  'level': role_level, 'book': book_url})
            post_resp1 = requests.post(self.b_url, data=role_js, headers=self.headers)
            #assert post_resp1.status_code == 201, f'Role create error {post_resp1.json()}'
            role_id = post_resp1.json()['id']
            self.role_url[role_id] = self.b_url + str(role_id)
            return post_resp1.status_code, post_resp1.json()

    def role_del(self, role_id: int = None):
        """delete role for id list"""
        if isinstance(role_id, int):
            if self.role_url[role_id] and self.check_book(self.role_url[role_id]):
                del_resp1 = requests.delete(self.role_url[role_id])
                #assert del_resp1.status_code == 204, "Role delete error"
                del self.role_url[role_id]
                return del_resp1.status_code

    def all_role_del(self):
        """del all role"""
        del_resp_all = {}
        for key in self.role_url.keys():
            if self.check_book(self.role_url[key]):
                del_resp1 = requests.delete(self.role_url[key])
                del_resp_all[key] = del_resp1
                #assert del_resp1.status_code == 204, "Role delete error"
        self.role_url = {}
        return del_resp_all



