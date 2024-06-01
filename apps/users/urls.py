from django.urls import path

from apps.users.views import UserListCreateAPIView,UserAddAutoParkView,UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='create_list_user'),
    path('/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='edit_user'),
    path('/<int:pk>/add_park', UserAddAutoParkView.as_view(), name='create_auto_park')
]