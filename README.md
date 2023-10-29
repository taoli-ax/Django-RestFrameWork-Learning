# Django-RestFrameWork-Learning


## jwt,simple jwt
https://blog.devgenius.io/json-web-token-jwt-in-django-rest-framework-drf-2896c56b596e
```text
    如何理解jwt的工作方式
```
1. simple_jwt 产生 token
    ```python
    ...
         path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
         ...
    ```
2. 客户端请求业务接口时需在headers中添加Authorization:Bear token,否则无法接通
     ```shell
     Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NTQ5NDkzLCJqdGkiOiIxNGRhYWZlZWM2OWI0MTRhODc1ZGYzYzg5MTg3YmRlMCIsInVzZXJfaWQiOjMsIm5hbWUiOiJ0b2xsZSJ9.ZjWA752ZDYMA_rZe9VWWhraNcSE7uBhL1cnUDltMwiU
     
     ```
3. 视图中的permission_class控制视图是否需要token的令牌验证
    ```python
    ...
        permission_classes = [permissions.IsAuthenticated]
        ...
    ```


## why jwt

```text 
    传统的cookie容易被低成本伪造，只要截获请求，就能拿走cookie, 而cookie是保存客户端身份的信息， 每次请求都要带着他才行，这进一步增加了漏洞
    jwt只需要在特定接口认证一次，如果用户名密码正确，则返回给你一串密文，让你保存
    理论上，只要获得这段密文，一样可以伪造请求，因此，即使定制token也无法避免被截获并伪造的危险。
    cookie跟token一样可以设置过期时间，这一点token并无优势
   
```

## hello jwt

https://www.zhihu.com/question/364616467