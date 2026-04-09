from rest_framework.serializers import ModelSerializer
from .models import Telefon


class TelefonSerializer(ModelSerializer):

    class Meta:
        model = Telefon
        fields = ["id", "name"]
