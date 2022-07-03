from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.
def one_week_hence()-> str:
    return timezone.now() + timezone.timedelta(days = 7)

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 100, unique = True, validators = [MinLengthValidator(1)])

    def get_absolute_url(self):
        return reverse('list', args = [self.id])

    def __repr__(self):
        return 'ToDoList(title: {}, user: {})'.format(self.title, self.user)

    def __str__(self):
        return self.__repr__()

class ToDoItem(models.Model):
    title = models.CharField(max_length = 100, unique = True, validators = [MinLengthValidator(1)])
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField(default = one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            'item-update', args = [str(self.todo_list.id), str(self.id)]
        )

    def __repr__(self):
        return 'ToDoItem(title: {}, due: {})'.format(self.title, self.due_date)

    def __str__(self):
        return self.__repr__()

    class Meta:
        ordering = ["due_date"]