from django.conf import urls
from django.urls import path
from .views import HomePageView, TodoCreateView, todo_delete_view, TodoUpdateView
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('todo/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/update/<int:pk>/', TodoUpdateView.as_view(), name='todo-edit'),
    path('todo/delete/<int:pk>/', todo_delete_view, name='todo-delete'),
]

