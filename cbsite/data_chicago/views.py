from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .models import LocationType1
from .forms import VariableChoices1, YearForm
import sqlite3
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

def get_year(request):
    form1 = YearForm
    return render(request, 'data_chicago/yr_dropdown_options.html', {'years': YearForm})
