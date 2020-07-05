# -*- encoding:utf-8 -*-
"""
@作者：leel
@文件名：urls.py
@时间：2020/7/4  20:36
@文档说明:
"""
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.demo),
    path('register/',views.register,name = 'register'),
    path('image_code/<uuid:img_id>/',views.image_code,name = 'image_code'),
]