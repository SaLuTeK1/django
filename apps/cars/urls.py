from django.urls import path

from apps.cars.views import CarListView, CarListCreateView

urlpatterns = [
    path('', CarListView.as_view(), name='cars'),
    path('/<int:pk>',CarListCreateView.as_view(), name='cars-create')
]