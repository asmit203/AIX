from django.urls import path
from mlmodel import views

urlpatterns=[
    path('', views.index, name='index'),
]