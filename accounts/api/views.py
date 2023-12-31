from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import viewsets
from accounts.api.serializers import LoginTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login


class AccountsViewSet(viewsets.ViewSet):
    # serializer_class = LoginTokenObtainPairSerializer
    permission_class = [permissions.AllowAny]

    @action(methods=['POST'], detail=False)
    def login(self, request):
        serializer = LoginTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            login(request, serializer.validated_data['user'])
            return Response({
                'success': True,
                'tokens': {
                    'refresh': serializer.validated_data['refresh'],
                    'access': serializer.validated_data['access'],
                },
                'user': serializer.validated_data['user'].username
            }, status=status.HTTP_200_OK)
