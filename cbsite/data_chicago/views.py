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
            crime = form.cleaned_data['crimefield']
            tooltips = form.cleaned_data['tooltipfield']
            datapoints = form.cleaned_data['datapointfield']
            request_list = [year, crime, tooltips, datapoints]
            load_map(year, crime, tooltips, datapoints)
            return HttpResponseRedirect('')
    else:
        form = InputForm()

    return render(request, 'data_chicago/loctype.html', {'form': form})

def load_map(year, crime, tooltips, datapoints):
    if tooltips == "Yes":
        tooltips = True
    elif tooltips == "No":
        tooltips = False
    if year != "":
        marp = chicago_data_functions.map_chicago_crime_db(tooltips, datapoints, year, crime)
        print(marp)
