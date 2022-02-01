from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Snippets
from .serializers import SnippetSerializer
# Create your views here.


class JSONResponse(HttpResponse):
    def __init__(self,data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)


@api_view(['POST','GET'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)
    elif request.method=='POST':

        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST','GET','DELETE'])
def snippet_detail(request,pk, format=None):
    """
    获取 更新 删除 一个 code snippet
    :param request:
    :param pk:
    :return:
    """
    try:
        snippet= Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
