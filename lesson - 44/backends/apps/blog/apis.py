# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals, print_function, division, absolute_import
from apps.models import Blog
import json


fields = ("id", "author", "title", "content", "category")


def get_blog(params):
    return Blog.objects.filter(pk=params.get("id")).values(*fields)[0]


def add_blog(params):
    Blog(
        author=params.get("author"),
        title=params.get("title"),
        content=params.get("content"),
        category=",".join(params.get("categories")),
    ).save()


def get_blog_list():
    return Blog.objects.all().values(*fields)


def get_params(request, *args):
    if request.method.lower() == "get":
        ret = {_: request.GET.get(_) for _ in args}
    else:
        if request.accepted_media_type == "application/json":
            ret = {_: json.loads(request.body).get(_) for _ in args}
        else:
            ret = {_: request.data.get(_) for _ in args}
    return ret
