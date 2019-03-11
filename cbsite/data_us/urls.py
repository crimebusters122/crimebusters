from django.urls import path
from . import views

urlpatterns = [
    path('', views.loc_type, name='location_type'),
]