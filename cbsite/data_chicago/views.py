from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .models import LocationType1
from .forms import VariableChoices1, YearForm, CrimeForm
import sqlite3
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

def get_year(request):
    form1 = YearForm
    return render(request, 'data_chicago/yr_dropdown_options.html', {'years': YearForm})

def get_crimes(request):
    form2 = CrimeForm
    return render(request, 'data_chicago/crime_dropdown_options.html', {'crimes': CrimeForm})
