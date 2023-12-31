from rest_framework import serializers
from cars.models import Cars


class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ('car_type', 'name')
