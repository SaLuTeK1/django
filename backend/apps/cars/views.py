from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarListSerializer, CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CarListSerializer
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer





