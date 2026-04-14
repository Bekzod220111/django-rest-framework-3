from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import TodoList
from .seralizers import TodoListSeralizer


class TodoListCreateApiView(ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSeralizer


class TodoDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSeralizer