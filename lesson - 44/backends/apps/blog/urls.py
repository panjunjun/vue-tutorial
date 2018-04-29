# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals, print_function, division, absolute_import
from django.conf.urls import url
from . import views


urlpatterns = [
    url("add/$", views.Add.as_view()),
    url("test/$", views.Test.as_view()),
    url("list/$", views.List.as_view()),
    url("$", views.Default.as_view()),
]
