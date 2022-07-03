from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('register/', views.RegisterPage.as_view(), name = 'register'),
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.ItemListView.as_view(), name = 'list'),
    # CRUD patterns for ToDoLists
    path("list/add/", views.ListCreate.as_view(), name = 'list-add'),
    path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete")
]