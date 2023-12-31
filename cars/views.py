# Create your views here.
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from cars.models import Cars
from cars.serializers import CarsSerializer


class CarViewSets(ModelViewSet):
    """
    用户请求该接口，需要先登录获取token，然后带上token请求获取接口正确响应
    """
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [permissions.IsAuthenticated]
    



