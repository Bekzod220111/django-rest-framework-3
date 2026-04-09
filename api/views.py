from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Telefon
from .seralizers import TelefonSerializer

# Create your views here.


class MyAPi(APIView):

    def get(self, request):
        telefon = Telefon.objects.all()
        data = TelefonSerializer(telefon, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = TelefonSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            name = ser.name
        msg = f"{name} telefon qoshildi."
        return Response({"message": msg})

    def put(self, request):
        try:
            new_name = request.data.get("new_name")
            id = request.data.get("id")
            telefon = Telefon.objects.get(id=id)
            if new_name:
                telefon.save()
            telefon.name = new_name
            telefon.save()
            return Response("Saqlandi chotkiy")
        except Telefon.DoesNotExist:
            return Response("kechirasiz telefon topilmadi.")
        except Exception as e:
            return Response("Nomalum xatolik: " + str(e))
