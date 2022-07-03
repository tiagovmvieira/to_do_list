from audioop import reverse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.urls import reverse_lazy

from .models import ToDoItem, ToDoList

from django.http.response import HttpResponseRedirect

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'todo_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'todo_app/register.html'
    form_class = UserCreationForm #specific form
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form: UserCreationForm)-> HttpResponseRedirect:
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs)-> HttpResponseRedirect:
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

class ListListView(LoginRequiredMixin, ListView):
    model = ToDoList
    context_object_name = 'todo_lists'
    template_name = 'todo_app/index.html'

    def get_queryset(self):
        return ToDoList.objects.filter(user = self.request.user)

class ListCreate(LoginRequiredMixin, CreateView):
    model = ToDoList
    fields = ['user', 'title']

    def get_context_data(self)-> dict:
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class ListDelete(LoginRequiredMixin, DeleteView):
    model = ToDoList
    success_url = reverse_lazy('index')

    template_name = 'todo_app/list_confirm_delete.html'

class ItemListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    template_name = 'todo_app/todo_list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id = self.kwargs["list_id"])

    def get_context_data(self)-> dict:
        context = super().get_context_data()
        context["todo_item"] = ToDoList.objects.get(id = self.kwargs["list_id"])
        return context

class ItemCreate(LoginRequiredMixin, CreateView):
    model = ToDoItem
    fields = ['todo_list', 'title', 'description', 'complete', 'due_date']


    def get_initial(self)-> dict:
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id = self.kwargs["list_id"])
        initial_data['todo_item'] = todo_list
        return initial_data


class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = ['todo_list', 'title', 'description', 'complete', 'due_date']

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = ToDoItem
    pass