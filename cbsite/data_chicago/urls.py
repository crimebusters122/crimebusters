from django.urls import path
from . import views

urlpatterns = [
    path('', views.stuff, name='Total form'),
    path('load_years', views.load_years, name='load_years'),
    path('load_crimes', views.load_crimes, name='load_crimes'),
    path('load_tooltips', views.load_tooltips, name='load_tooltips'),
]