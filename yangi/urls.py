from django.urls import path
from . import views

urlpatterns = [
    path('todolist/', views.TodoListCreateApiView.as_view()),
    path('todolist/<int:pk>/', views.TodoDetailApiView.as_view()),
]   