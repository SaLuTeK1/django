from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from apps.cars.serializers import CarSerializer
from apps.cars.models import CarModel

from rest_framework import status

class CarListCreateView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

