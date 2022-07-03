from django.contrib.auth.models import User
from django.test import TestCase

from todo_app.models import ToDoItem, ToDoList

class TestModels(TestCase):

    @classmethod
    def setUp(cls):
        ToDoList.objects.create(
            user = User.objects.create_user(username = 'user', password = '12345'),
            title = 'to_do_list_title'
            )
        
        ToDoItem.objects.create(
            title = 'to_do_item_title'
        )

    def test_to_do_list_title_label(self):
        to_do_list = ToDoList.objects.get(id = 1)
        title_label = to_do_list._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_to_do_list_user_label(self):
        to_do_list = ToDoList.objects.get(id = 1)
        user_label = to_do_list._meta.get_field('user').verbose_name
        self.assertEqual(user_label, 'user')

    def test_to_item_title_label(self):
        to_do_item = ToDoItem.objects.get(id = 1)
        title_label = to_do_item._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    """
    def test_to_do_item_title_label(self):
        to_do_item = ToDoItem.objects.get(to_do_list_id = 1, to_do_item_id = 1)
        title_label = to_do_item._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')
    """
    



"""
    @classmethod
    def setUp(cls):
        cls.to_do_list = ToDoList.objects.create(
            user = 'user',
            title = 'to_do_list_title'
        )
        cls.to_do_list.save()

        cls.to_do_item = ToDoItem.objects.create(
            title = 'to_do_item_title',
            description = 'to_do_item_description',
            complete = False,
            created_at = 'não sei que colocar aqui',
            todo_list = cls.to_do_list
        )

    def test_1(self):
        self.assertEqual(self.to_do_item.todo_list, self.to_do_list)
"""