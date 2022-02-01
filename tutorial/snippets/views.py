from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippets
from .serializers import SnippetSerializer
# Create your views here.


class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

@csrf_exempt
def snippet_list(request):
    if request.method=='GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return JSONResponse(serializer.data)
    elif request.method=='POST':

        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors,status=500)

@csrf_exempt
def snippet_detail(request,pk):
    """
    获取 更新 删除 一个 code snippet
    :param request:
    :param pk:
    :return:
    """
    try:
        snippet= Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)

    elif request.method=='DELETE':
        snippet.delete()
        return HttpResponse(status=204)
