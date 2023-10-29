import datetime
from django.shortcuts import render
# Create your views here.
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from cars.models import Cars
from cars.serializers import CarsSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import  JWTAuthentication


class CarViewSets(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [permissions.IsAuthenticated]
    



