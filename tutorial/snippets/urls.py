from .views import *
from django.urls import path


urlpatterns = [
    path(r'snippets/', snippet_list),
    path(r'detail/<int:pk>', snippet_detail)
]