from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .models import LocationType1, LocationType2
from .forms import VariableChoices1, VariableChoices2, LocationTypeForm
import sqlite3
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

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
        return HttpResponseRedirect('')
    else:
        form_1 = VariableChoices1()
    forms = {'form_1': form_1}
    return render(request, 'data_us/loctype.html', forms)


def load_locs_1(request):
    loc_type = request.GET.get('location_type_1')
    if loc_type == 'country':
          locs = ['United States']
    elif loc_type == 'state':
        locs = states
    elif loc_type == 'city':
        locs = get_cities()
    return render(request, 'data_us/loc_dropdown_options.html', {'locs': locs})

def load_var_types_1(request):
    loc_type = request.GET.get('location_type_1')
    if loc_type == 'state':
        var_types = ['Crime']
    elif loc_type == 'country':
        var_types = ['Arrest', 'Crime']
    elif loc_type == 'city':
        var_types = ['Arrest', 'Crime']
    return render(request, 'data_us/var_type_dropdown_options.html', \
                {'var_types': var_types})


def load_vars_1(request):
    var_type = request.GET.get('variable_type_1')
    if var_type == 'state_crime':
        variables = ['Violent Crime Total', 'Murder and Nonnegligent Manslaughter', \
                    'Rape', 'Robbery', 'Aggravated Assault', 'Property Crime Total', \
                    'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft', \
                    'Violent Crime Rate', 'Murder and Nonnegligent Manslaughter Rate', \
                    'Rape Rate', 'Robbery Rate', 'Aggravated Assault Rate', \
                    'Property Crime Rate', 'Burglary Rate', 'Larceny-Theft Rate', \
                    'Motor Vehicle Theft Rate']
    elif var_type == 'city_crime':
        variables = ['Violent Crime Total', 'Murder and Nonnegligent Manslaughter', \
                'Rape', 'Robbery', 'Aggravated Assault', 'Property Crime Total', \
                'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft', \
                'Violent Crime Rate', 'Murder and Nonnegligent Manslaughter Rate', \
                'Rape Rate', 'Robbery Rate', 'Aggravated Assault Rate', \
                'Property Crime Rate', 'Burglary Rate', 'Larceny-Theft Rate', \
                'Motor Vehicle Theft Rate']
    elif var_type == 'city_arrest':
        variables = ['Violent Crime Total', 'Murder and Nonnegligent Manslaughter', \
                    'Rape', 'Robbery', 'Aggravated Assault', 'Property Crime Total', \
                    'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft']
    elif var_type == 'us_crime':
        variables = ['Violent Crime Total', 'Murder and Nonnegligent Manslaughter', \
                'Rape', 'Robbery', 'Aggravated Assault', 'Property Crime Total', \
                'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft', \
                'Violent Crime Rate', 'Murder and Nonnegligent Manslaughter Rate', \
                'Rape Rate', 'Robbery Rate', 'Aggravated Assault Rate', \
                'Property Crime Rate', 'Burglary Rate', 'Larceny-Theft Rate', \
                'Motor Vehicle Theft Rate']
    elif var_type == 'us_arrest':
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
    return render(request, 'data_us/vars_dropdown_options.html', \
            {'variables': variables})
