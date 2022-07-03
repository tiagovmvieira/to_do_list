from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    
    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.login_url = reverse('login')
        cls.logout_url = reverse('logout')
        cls.register_url = reverse('register')
        cls.list_todolist_url = reverse('index')
        cls.list_todolist_id_url = reverse('list', args=[0])

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_app/login.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302) #redirecting page

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_app/register.html')

    def test_list_todolists_GET(self):
        response = self.client.get(self.list_todolist_url)

        self.assertEquals(response.status_code, 302) #redirecting page
        # self.assertTemplateUsed(response, 'todo_app/index.html')
        
    def test_todolist_id_url_GET(self):
        response = self.client.get(self.list_todolist_id_url)
        
        # self.assertTemplateUsed(response, 'todo_app/todo_list.html')

        self.assertEquals(response.status_code, 302) #redirecting page