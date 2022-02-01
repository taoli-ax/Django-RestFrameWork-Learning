from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippets
from .serializers import SnippetSerializer


# Create your views here.


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class SnippetList(APIView):

    def get(self, request, format=None):
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):

    def get_object(self,pk):
        try:
            snippet = Snippets.objects.get(pk=pk)
        except Snippets.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk,format=None):
        snippet=self.get_object(pk=pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,pk):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
