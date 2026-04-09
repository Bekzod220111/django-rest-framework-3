from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Telefon, Mashina
from .seralizers import TelefonSerializer, MashinaSerializer


class MyAPi(APIView):

    def get(self, request):
        telefon = Telefon.objects.all()
        data = TelefonSerializer(telefon, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = TelefonSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            name = ser.validated_data.get("name")
        msg = f"{name} telefon qoshildi."
        return Response({"message": msg})

    def put(self, request):
        try:
            new_name = request.data.get("new_name")
            id = request.data.get("id")
            telefon = Telefon.objects.get(id=id)
            if new_name:
                telefon.name = new_name
            telefon.save()
            return Response("Saqlandi chotkiy")
        except Telefon.DoesNotExist:
            return Response("kechirasiz telefon topilmadi.")
        except Exception as e:
            return Response("Nomalum xatolik: " + str(e))


class MashinaAPIView(APIView):

    def get(self, request):
        mashina = Mashina.objects.all()
        data = MashinaSerializer(mashina, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = MashinaSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)


class MashinaDetailApiView(APIView):

    def get(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina_ser = MashinaSerializer(mashina).data
            return Response(mashina_ser, status=status.HTTP_200_OK)
        except: # noqa
            return Response(
            {"error": "Mashina does not exist"},status=status.HTTP_400_BAD_REQUEST, # noqa
            )

    def put(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina_ser = MashinaSeralizer(data=request.data, instance=mashina)
            if mashina_ser.is_valid():
                mashina_ser.save()
            else:
                return Response(
                    mashina_ser.errors,
                    status=status.HTTP_400_BAD_REQUEST,  # noqa
                )
            return Response(mashina_ser.data, status=status.HTTP_200_OK)
        except:  # noqa
            return Response(
                {"error": "Mashina does not exist"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa
            )
    
    def patch(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina_ser = MashinaSeralizer(data=request.data, instance=mashina, partial=True)
            if mashina_ser.is_valid():
                mashina_ser.save()
            else:
                return Response(
                    mashina_ser.errors,
                    status=status.HTTP_400_BAD_REQUEST,  # noqa
                )
            return Response(mashina_ser.data, status=status.HTTP_200_OK)
        except:  # noqa
            return Response(
                {"error": "Mashina does not exist"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa
                )

    
    def delete(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina.delete()
            return Response(
                {"message": f"{mashina.name} deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except:  # noqa
            return Response(
                {"error": "Mashina does not exist"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa
            )