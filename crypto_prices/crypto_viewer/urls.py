from django.urls import path, include
from django.contrib import admin

from crypto_viewer import views

urlpatterns = [
    path('',views.index, name='index'),
]