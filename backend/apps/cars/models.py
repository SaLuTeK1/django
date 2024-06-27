from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.choises import CarChoices
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)
    brand = models.CharField(max_length=20,validators=[V.MinLengthValidator(2)])
    price = models.IntegerField(validators=[V.MinValueValidator(0) , V.MaxValueValidator(5000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990),V.MaxValueValidator(datetime.now().year)])
    capacity = models.IntegerField()
    body_type = models.CharField(max_length=20,choices=[*CarChoices.choices])
    engine = models.FloatField()

    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    # CASCADE SETNULL PROTECTED
    objects = CarManager()

    