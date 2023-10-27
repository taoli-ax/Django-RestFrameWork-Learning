from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from cars.models import Cars
from cars.serializers import CarsSerializer


class CarViewSets(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [permissions.AllowAny]

