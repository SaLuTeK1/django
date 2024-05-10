from django.urls import path
from cars.views import CarListView, CarDetailView

urlpatterns = [
    path('cars', CarListView.as_view()),
    path('carDetail/<int:pk>', CarDetailView.as_view())
]
