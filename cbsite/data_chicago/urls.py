from django.urls import path
from . import views

urlpatterns = [
    path('', views.stuff, name='Total form')
]