from ast import Delete
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
    template_name = 'base/task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

    template_name = 'base/task_detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    template_name = 'base/task_form.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    template_name = 'base/task_form.html'

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    template_name = 'base/task_confirm_delete.html'