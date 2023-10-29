from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):

#         return super().validate(attrs)



class LoginTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    原文链接: https://blog.csdn.net/u014783334/article/details/124841293
    """
    @classmethod
    def get_token(cls, user):
        """
        此方法往token的有效负载 payload 里面添加数据
        若自定义了用户表，可以在这里面添加用户邮箱，性别，年龄等可以公开的信息
        这部分放在token里面是可以被解析的，所以不要放比较私密的信息
        :param user: 用戶信息
        :return: token
        """
        token = super().get_token(user)
        # 添加个人信息
        token['name'] = user.username
        # token['mobile'] = user.mobile
        return token
        
    def validate(self, attrs):
        '''此方法是 响应数据结构，默认返回只有 access 和 refresh'''
        data = super().validate(attrs=attrs)
        # 获取Token对象
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        # 令牌到期时间
        data['expire'] = refresh.access_token.payload['exp']  # 有效期
        # 用户名
        print(self.user)
        data['user_id'] = self.user.id
        # 手机号
        # data['mobile'] = self.user.mobile
        return data