from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .models import LocationType1
from .forms import InputForm
import sqlite3
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from . import chicago_data_functions

def stuff(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['yearfield']
            crumb = form.cleaned_data['crimefield']
            tooltips = form.cleaned_data['tooltipfield']
            datapoints = form.cleaned_data['datapointfield']
            load_map(year, crumb, tooltips, datapoints)
            return HttpResponseRedirect('')
    else:
        form = InputForm()

    return render(request, 'data_chicago/loctype.html', {'form': form})

def load_map(year, crumb, tooltips, datapoints):
    if tooltips == "Yes":
        tooltips = False
    elif tooltips == "No":
        tooltips = True
    if year != "":
        marp = chicago_data_functions.map_chicago_crime_db(
            quick = tooltips, 
            num = datapoints, 
            year = year,
            prim_type = crumb
            )
        print(marp)
