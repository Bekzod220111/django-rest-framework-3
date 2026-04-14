from rest_framework.serializers import ModelSerializer  
from .models import TodoList


class TodoListSeralizer(ModelSerializer):

    class Meta:
        model = TodoList
        fields = "__all__"