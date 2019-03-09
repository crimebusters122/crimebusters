from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_loc_type, name='location type'),
]