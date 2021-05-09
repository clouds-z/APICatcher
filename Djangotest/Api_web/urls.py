"""
author： xjz
date: 2021-04-20
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('content', views.article_content)

]
