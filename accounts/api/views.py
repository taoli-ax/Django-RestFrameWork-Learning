from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import viewsets
from accounts.api.serializers import LoginTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from django.contrib.auth.models import User



class AccountsViewSet(TokenObtainPairView, viewsets.ViewSet):
    serializer_class = LoginTokenObtainPairSerializer
    permission_class = [permissions.AllowAny]

    @action(methods=['POST'],detail=False)
    def login(self,request):
        serializer = LoginTokenObtainPairSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'error': serializer.error_messages,
                'message':'please check input'
            })
        user_id = serializer.validated_data['user_id']
        user = User.objects.get(pk=user_id)
        login(request, user)

        return Response({
            'success': True,
            'tokens': {
                'refresh': serializer.validated_data['refresh'],
                'access': serializer.validated_data['access'],
            },
            'user_id':serializer.validated_data['user_id']
        }, status=status.HTTP_200_OK)







