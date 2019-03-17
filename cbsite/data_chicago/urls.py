from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_form, name='Total form'),
    path('show_marp', views.load_data, name="load_data"),
]