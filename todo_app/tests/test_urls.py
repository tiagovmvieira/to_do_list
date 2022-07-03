from django.test import TestCase
from django.urls import reverse, resolve

from django.contrib.auth.views import LogoutView

from .. import views

class TestUrls(TestCase):

    @classmethod
    def setUp(cls):
        cls.login_url = reverse('login')
        cls.logout_url = reverse('logout')
        cls.register_url = reverse('register')
        cls.index_url = reverse('index')
        cls.list_todo_list_id_url = reverse('list', args = [0])
        cls.add_list_url = reverse('list-add')
        cls.delete_list_url = reverse('list-delete', args = [0])

    # General Urls
    def test_login_url_resolves(self):
        self.assertEquals(resolve(self.login_url).func.view_class, views.CustomLoginView)
    
    def test_logout_url_resolves(self):
        self.assertEquals(resolve(self.logout_url).func.view_class, LogoutView)

    def test_register_url_resolves(self):
        self.assertEquals(resolve(self.register_url).func.view_class, views.RegisterPage)

    def test_list_task_url_resolves(self):
        self.assertEquals(resolve(self.index_url).func.view_class, views.ListListView)

    def test_list_todolist_id_url_resolves(self):
        self.assertEquals(resolve(self.list_todo_list_id_url).func.view_class, views.ItemListView)

    # CRUD Urls for ToDoLists
    def test_add_list_url_resolves(self):
        self.assertEquals(resolve(self.add_list_url).func.view_class, views.ListCreate)

    def test_delete_list_url_resolves(self):
        self.assertEquals(resolve(self.delete_list_url).func.view_class, views.ListDelete)