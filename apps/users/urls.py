from django.urls import path

from apps.users.views import UserAddAvatarView, UserBlock, UserListCreateAPIView, UserUnBlock

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='CreateUser'),
    path('/avatars', UserAddAvatarView.as_view(), name='avatar_add'),
    path('/block/<int:pk>', UserBlock.as_view(), name='block_user'),
    path('/unblock/<int:pk>', UserUnBlock.as_view(), name='unblock_user'),
]
