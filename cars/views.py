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
    




class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    """
    继承父类的 post 方法,改变客户端的响应
    依赖于 CustomTokenObtainPairSerializer 的 validate 方法
    validate的核心其实是在 django backend 中匹配到用户信息
    """
    def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            response_data = {
                'message': f'{serializer.validated_data["username"]},这是顽童你知道的 ! expired: {datetime.datetime.fromtimestamp(serializer.validated_data["expire"])}',
                'tokens': {
                    'refresh': serializer.validated_data['refresh'],
                    'access': serializer.validated_data['access'],
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
