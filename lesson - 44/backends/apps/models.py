# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals, print_function, division, absolute_import
from django.db import models


class Blog(models.Model):
    author = models.CharField(help_text="作者", max_length=32)
    title = models.CharField(help_text="标题", max_length=256)
    content = models.TextField(help_text="正文")
    category = models.CharField(help_text="分类", max_length=32)
