from django import forms
from .models import LocationType, Location, Variable
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


class LocationTypeForm(forms.Form):
    location_type = forms.CharField(label="Location Type", \
                    widget=forms.Select(choices=[('country', 'Country'), \
                           ('state', 'State'), ('city', 'City')]))

class LocationForm(forms.ModelForm):
    class Meta:
        model = LocationType
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.none()
