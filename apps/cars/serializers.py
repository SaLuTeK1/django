from rest_framework import serializers
from apps.cars.models import CarModel

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id','brand','price','year','capacity','engine','body_type')

    def validate(self, attrs):
        print(attrs)
        return attrs

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields=('id','brand','price','year')
