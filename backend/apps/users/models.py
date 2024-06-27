from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel
from core.services.upload_avatar import upload_avatar

from apps.users.managers import UserManager


# Create your models here.
class UserModel(PermissionsMixin, AbstractBaseUser, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)

    password = models.CharField( max_length=128, validators=[
        V.RegexValidator(*RegexEnum.PASSWORD.value)
    ])

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=30, validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])
    surname = models.CharField(max_length=30, validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=upload_avatar, blank=True, validators=(
        V.FileExtensionValidator(['jpg', 'gif', 'png', 'jpeg']),
    ))
