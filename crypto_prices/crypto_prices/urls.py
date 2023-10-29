from django.urls import path
from crypto_viewer import views

urlpatterns = [
    path('', views.index, name='index'),
]