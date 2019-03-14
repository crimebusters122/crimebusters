from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import graph
from . import models
from .models import LocationType1, LocationType2
from .forms import VariableChoices1, VariableChoices2, LocationTypeForm, NextPageForm
import sqlite3
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect
from urllib.parse import urlencode
from . import simple_graph

crime_variables = ['Violent Crime Total', 'Murder and Nonnegligent Manslaughter', \
                    'Rape', 'Robbery', 'Aggravated Assault', 'Property Crime Total', \
                    'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft', \
                    'Violent Crime Rate', 'Murder and Nonnegligent Manslaughter Rate', \
                    'Rape Rate', 'Robbery Rate', 'Aggravated Assault Rate', \
                    'Property Crime Rate', 'Burglary Rate', 'Larceny-Theft Rate', \
                    'Motor Vehicle Theft Rate']


def get_cities():
    conn = sqlite3.connect('crimebusters_data.db')
    c = conn.cursor()
    cities = c.execute('SELECT DISTINCT City FROM bjs_city')
    tup_list = cities.fetchall()
    one_city = []
    for tup in tup_list:
        city = tup[0]
        for char in '()':
            city = city.replace(char, '')
        one_city.append(city)
    return one_city

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', \
          'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', \
          'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', \
          'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', \
          'VA', 'VT', 'WA', 'WV', 'WI', 'WY']

def get_loc_type(request):
    if request.method == 'POST':
        form_1 = VariableChoices1(request.POST)
        form_2 = VariableChoices2(request.POST)
        return HttpResponseRedirect('')
    else:
        form_1 = VariableChoices1()
        form_2 = VariableChoices2()
    forms = {'form_1': form_1, 'form_2': form_2}
    return render(request, 'data_us/loctype.html', forms)


def load_locs_1(request):
    loc_type = request.GET.get('location_type_1')
    if loc_type == 'country':
          locs = ['United States']
          zipped = [('US', 'United States')]
    elif loc_type == 'state':
        locs = states
        zipped = zip(locs, locs)
    elif loc_type == 'city':
        locs = get_cities()
        stripped = []
        for loc in locs:
            loc_l = loc.lower()
            loc_r = loc_l.replace(' ', '_')
            stripped.append(loc_r)
        zipped = zip(stripped, locs)
    return render(request, 'data_us/loc_dropdown_options.html', {'zipped': zipped})

def load_locs_2(request):
    loc_type = request.GET.get('location_type_2')
    if loc_type == 'country':
          locs = ['United States']
          zipped = [('US', 'United States')]
    elif loc_type == 'state':
        locs = states
        zipped = zip(locs, locs)
    elif loc_type == 'city':
        locs = get_cities()
        stripped = []
        for loc in locs:
            loc_l = loc.lower()
            loc_r = loc_l.replace(' ', '_')
            stripped.append(loc_r)
        zipped = zip(stripped, locs)
    return render(request, 'data_us/loc_dropdown_options.html', {'zipped': zipped})

def load_var_types_1(request):
    loc_type = request.GET.get('location_type_1')
    if loc_type == 'state':
        var_types = ['Crime']
    elif loc_type == 'country':
        var_types = ['Arrest', 'Crime']
    elif loc_type == 'city':
        var_types = ['Arrest', 'Crime']
    stripped = []
    for var_type in var_types:
        var_type_l = var_type.lower()
        var_type_r = var_type_l.replace(' ', '_')
        stripped.append(var_type_r)
    zipped = zip(stripped, var_types)
    return render(request, 'data_us/var_type_dropdown_options.html', \
                {'zipped': zipped})

def load_var_types_2(request):
    loc_type = request.GET.get('location_type_2')
    if loc_type == 'state':
        var_types = ['Crime']
    elif loc_type == 'country':
        var_types = ['Arrest', 'Crime']
    elif loc_type == 'city':
        var_types = ['Arrest', 'Crime']
    stripped = []
    for var_type in var_types:
        var_type_l = var_type.lower()
        var_type_r = var_type_l.replace(' ', '_')
        stripped.append(var_type_r)
    zipped = zip(stripped, var_types)
    return render(request, 'data_us/var_type_dropdown_options.html', \
                {'zipped': zipped})

def load_vars_1(request):
    var_type = request.GET.get('variable_type_1')
    loc_type = request.GET.get('location_type_1')
    if loc_type == 'state':
        variables = crime_variables
    elif loc_type == 'city':
        if var_type == 'Crime':
            variables = crime_variables
        else:
            variables = ['Violent Crime Total', 'Murder and Nonnegligent Manslaughter', \
                    'Rape', 'Robbery', 'Aggravated Assault', 'Property Crime Total', \
                    'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft']
    elif loc_type == 'country':
        if var_type == 'Crime':
            variables = crime_variables
        else:
            variables = ['Total Arrests', 'Violent Crime Index', \
                    'Murder and Nonnegligent Manslaughter', 'Rape', 'Robbery', \
                    'Aggravated Assault', 'Property Crime Index', 'Burglary', \
                    'Larceny-Theft', 'Motor Vehicle Theft', 'Arson', \
                    'Forgery and Counterfeiting', 'Fraud', 'Embezzlement', \
                    'Stolen Property', 'Vandalism', 'Weapons', 'Prostitution', \
                    'Sex Offenses', 'Drug Abuse Violations', \
                    'Driving Under the Influence', 'Gambling', 'Liquor Laws', \
                    'Drunkenness', 'Disorderly Conduct', 'Vagrancy', \
                    'Curfew and Loitering', 'Runaways']
    stripped = []
    for var in variables:
        var_l = var.lower()
        var_r = var_l.replace(' ', '_')
        stripped.append(var_r)
    zipped = zip(stripped, variables)
    return render(request, 'data_us/vars_dropdown_options.html', \
            {'zipped': zipped})

def load_vars_2(request):
    var_type = request.GET.get('variable_type_2')
    loc_type = request.GET.get('location_type_2')
    loc_1 = request.GET.get('location_1')
    loc_2 = request.GET.get('location_2')
    if loc_type == 'state':
        variables = crime_variables
    elif loc_type == 'city':
        if var_type == 'Crime':
            variables = crime_variables
        else:
            variables = ['Violent Crime Total', 'Murder and Nonnegligent Manslaughter', \
                    'Rape', 'Robbery', 'Aggravated Assault', 'Property Crime Total', \
                    'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft']
    elif loc_type == 'country':
        if var_type == 'Crime':
            variables = crime_variables
        else:
            variables = ['Total Arrests', 'Violent Crime Index', \
                    'Murder and Nonnegligent Manslaughter', 'Rape', 'Robbery', \
                    'Aggravated Assault', 'Property Crime Index', 'Burglary', \
                    'Larceny-Theft', 'Motor Vehicle Theft', 'Arson', \
                    'Forgery and Counterfeiting', 'Fraud', 'Embezzlement', \
                    'Stolen Property', 'Vandalism', 'Weapons', 'Prostitution', \
                    'Sex Offenses', 'Drug Abuse Violations', \
                    'Driving Under the Influence', 'Gambling', 'Liquor Laws', \
                    'Drunkenness', 'Disorderly Conduct', 'Vagrancy', \
                    'Curfew and Loitering', 'Runaways']
    if loc_1 == loc_2:
        variables = ['Time'] + variables
    stripped = []
    for var in variables:
        var_l = var.lower()
        var_r = var_l.replace(' ', '_')
        stripped.append(var_r)
    zipped = zip(stripped, variables)
    return render(request, 'data_us/vars_dropdown_options.html', \
            {'zipped': zipped})

def load_graph_vars(request):
    print(request)
    graph_vars = []
    var_type_1 = request.GET.get('variable_type_1')
    var_type_2 = request.GET.get('variable_type_2')
    loc_type_1 = request.GET.get('location_type_1')
    if loc_type_1 == 'country':
        loc_type_1 = 'national'
    loc_type_2 = request.GET.get('location_type_2')
    if loc_type_2 == 'country':
        loc_type_2 = 'national'
    loc_1 = request.GET.get('location_1')
    loc_2 = request.GET.get('location_2')
    var_1 = request.GET.get('variable_1')
    var_2 = request.GET.get('variable_2')
    graph_vars.append(('variable_type_1', var_type_1))
    graph_vars.append(('variable_type_2', var_type_2))
    graph_vars.append(('location_type_1', loc_type_1))
    graph_vars.append(('location_type_2', loc_type_2))
    graph_vars.append(('location_1', loc_1))
    graph_vars.append(('location_2', loc_2))
    graph_vars.append(('variable_1', var_1))
    graph_vars.append(('variable_2', var_2))   
    loc_1 = loc_1.replace('_', ' ').capitalize()
    loc_2 = loc_2.replace('_', ' ').capitalize()
    var_1 = var_1.replace('_', ' ').capitalize()
    var_2 = var_2.replace('_', ' ').capitalize()
    print(var_1)
    print(var_2)
    simple_graph.simple(1)
    graph.make_graph(var_type_1, loc_type_1, var_1, loc_1, var_type_2, \
            loc_type_2, var_2, loc_2)
    return render(request, 'data_us/go_to_graph.html', {'graph_vars': graph_vars})

def load_graph(request):
    if request.GET.get('btn'):
        var_type_1 = request.GET.get('variable_type_1')
        var_type_1.replace('_', ' ').title()
        var_type_2 = request.GET.get('variable_type_2')
        var_type_2.replace('_', ' ').title()
        loc_type_1 = request.GET.get('location_type_1')
        loc_type_1.replace('_', ' ').title()
        loc_type_2 = request.GET.get('location_type_2')
        loc_type_2.replace('_', ' ').title()
        loc_1 = request.GET.get('location_1')
        loc_1.replace('_', ' ').title()
        loc_2 = request.GET.get('location_2')
        loc_2.replace('_', ' ').title()
        var_1 = request.GET.get('variable_1')
        var_1.replace('_', ' ').title()
        var_2 = request.GET.get('variable_2')
        var_2.replace('_', ' ').title()
        loaded = graph.make_graph(var_type_1, loc_type_1, var_1, loc_1, var_type_2, \
                    loc_type_2, var_2, loc_2)
    return render(request, 'data_us/graph.html', {'loaded': loaded})
