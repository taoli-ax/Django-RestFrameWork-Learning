from .models import Snippets
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = '__all__'
