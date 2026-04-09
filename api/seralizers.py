from rest_framework.serializers import ModelSerializer
from .models import Telefon, Mashina


class TelefonSerializer(ModelSerializer):
    class Meta:
        model = Telefon
        fields = ["id", "name"]


class MashinaSerializer(ModelSerializer):
    class Meta:
        model = Mashina
        fields = "__all__"
