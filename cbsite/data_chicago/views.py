from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import folium

from .forms import InputForm
import sqlite3
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.shortcuts import render_to_response
from . import chicago_data_functions

def make_form(request):
    '''
    This is the initial loader for the form. It just makes the form and 
    calls the Django template.
    '''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['yearfield']
            crumb = form.cleaned_data['crimefield']
            tooltips = form.cleaned_data['tooltipfield']
            datapoints = form.cleaned_data['datapointfield']
            return HttpResponseRedirect('')
    else:
        form = InputForm()
        return render(request, 'data_chicago/mapchoices.html', {'form': form})

def load_data(request):
    '''
    Loads the map from our request. Gets the inputs from the form and calls
    the folium map making function.
    '''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['yearfield']
            if year == 'ALL YEARS':
                year = None
            crumb = form.cleaned_data['crimefield']
            if crumb == 'ALL CRIMES':
                crumb = False
            tooltips = form.cleaned_data['tooltipfield']
            datapoints = form.cleaned_data['datapointfield']
            if tooltips == "yes":
                tooltips = False
            elif tooltips == "no":
                tooltips = True
            marp = chicago_data_functions.map_chicago_crime_db(
                quick = tooltips, 
                num = datapoints, 
                year = year,
                prim_type = crumb
                )
            if type(marp) != str:
                meep = marp.get_root().render()
            else:
                meep = marp
            return render(request, "data_chicago/mapchoices.html", {
                "form": form, "meep": meep})
            return HttpResponseRedirect('')
    else:
        form = InputForm()
