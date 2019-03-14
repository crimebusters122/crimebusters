from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .models import LocationType1
from .forms import FormThing
import sqlite3
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

def stuff(request):
    form1 = FormThing
    return render(request, 'data_chicago/loctype.html', {'Form_1': FormThing})

def load_years(request):
    return render(request, 'data_chicago/yr_dropdown_options.html', {'years': years})

def load_crimes(request):
    return render(request, 'data_chicago/crime_dropdown_options.html', {'crimes': crimes})

def load_tooltips(request):
    return render(request, 'data_chicago/tooltip_dropdown_options.html', {'tooltips': tooltips})