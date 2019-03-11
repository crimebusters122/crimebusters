from django import forms
from django.forms import ModelForm
from . import models
from .models import LocationType
import sqlite3

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
    two_city = []
    for city in one_city:
        two_city.append((city, city))
    return two_city

states = [('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), \
          ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), \
          ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), \
          ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), \
          ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), \
          ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), \
          ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), \
          ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), \
          ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), \
          ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')]

class LocationTypeForm(forms.Form):
    location_type = forms.CharField(label="Location Type", \
                    widget=forms.Select(choices=[('country', 'Country'), \
                            ('state', 'State'), ('city', 'City')]))

class LocationForm(forms.Form):
    cities = forms.CharField(label='City', \
            widget=forms.Select(choices=get_cities()))
