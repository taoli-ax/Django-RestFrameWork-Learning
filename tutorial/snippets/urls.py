from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
from django.urls import path


urlpatterns = [
    path(r'snippets/', SnippetList.as_view()),
    path(r'detail/<int:pk>', SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)