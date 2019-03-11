from django.urls import path
from . import views

urlpatterns = [
    path('', views.var_type, name='variable type')
]