# app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_view, name='stats'),
]