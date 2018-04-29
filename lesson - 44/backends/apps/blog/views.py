# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals, print_function, division, absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from . import apis


class Add(APIView):
    permission_classes = [permissions.AllowAny]

    @classmethod
    def post(cls, request):
        params = apis.get_params(request, "title", "content", "author", "categories")
        return Response(apis.add_blog(params))


class Test(APIView):
    permission_classes = [permissions.AllowAny]

    @classmethod
    def get(cls, request):
        return Response("ok")


class List(APIView):
    permission_classes = [permissions.AllowAny]

    @classmethod
    def get(cls, request):
        return Response(apis.get_blog_list())


class Default(APIView):
    permission_classes = [permissions.AllowAny]

    @classmethod
    def get(cls, request):
        params = apis.get_params(request, "id")
        return Response(apis.get_blog(params))
