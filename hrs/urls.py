#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : urls.py
# @Time      : 2018/6/4 15:57
# @software  : PyCharm

from django.urls import path
from hrs import views


urlpatterns = [
    path('', views.index, name='index'),
]