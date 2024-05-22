from django.urls import path
from apps.auto_parks.views import AutoParkListCreateView,AutoParkAddCarViev

urlpatterns = [
    path('',AutoParkListCreateView.as_view(),name='auto_park_list_create'),
    path('/<int:pk>/add_car',AutoParkAddCarViev.as_view(),name='auto_park_add_car'),

]