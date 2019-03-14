from django import forms
from django.forms import ModelForm
from . import models
from .models import LocationType1, Location1, VariableType1, VariableChoices1, \
                    LocationType2, Location2, VariableType2, VariableChoices2, \
                    NextPage
from smart_selects.db_fields import ChainedForeignKey
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

def get_location_choices(ModelForm):
    if self.fields['location_type'] == 'Country':
        self.fields['location'] = forms.CharField(label="Location", \
                      widget=forms.Select(choices=[('us', 'United States')]))
    elif self.fields['location_type'] == 'State':
        self.fields['location'] = forms.CharField(label="Location", \
                    widget=forms.Select(choices=states))
    elif self.fields['location_type'] == 'City':
        self.fields['location'] = forms.CharField(label="Location", \
                    widget=forms.Select(choices=get_cities()))


class VariableChoices1(forms.ModelForm):
    class Meta:
        model = models.VariableChoices1
        fields = ['location_type_1', 'location_1', 'variable_type_1', 'variable_1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location_type_1'] = forms.CharField(label="Location Type", \
                    widget=forms.Select(choices=[('country', 'Country'), \
                            ('state', 'State'), ('city', 'City')]))
        self.fields['location_1'] = forms.CharField(label="Location", \
                    widget=forms.Select(choices=[]))
        self.fields['variable_type_1'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[]))
        self.fields['variable_1'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=[]))

        if 'location_type_1' in self.data:
          try:
            loc_type = self.data.get('location_type_1')
            if loc_type == 'Country':
              self.fields['location_1'] = forms.CharField(label="Location", \
                    widget=forms.Select(choices=[('us', 'United States')]))
              self.fields['variable_type_1'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[('us_arrest', 'Arrest'), \
                            ('us_crime', 'Crime')]))
            elif loc_type == 'State':
              self.fields['location_1']= forms.CharField(label="Location", \
                    widget=forms.Select(choices=states))
              self.fields['variable_type_1'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[('state_crime', 'Crime')]))
            elif loc_type == 'City':
              self.fields['location_1']= forms.CharField(label="Location", \
                    widget=forms.Select(choices=get_cities()))
              self.fields['variable_type_1'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[('city_arrest', 'Arrest'), \
                            ('city_crime', 'Crime')]))
          except (ValueError, TypeError):
            pass

        if 'variable_type_1' in self.data:
          try:
            loc_type = self.data.get('location_type_1')
            var_type = self.data.get('variable_type_1')
            if loc_type == 'Country':
              if var_type == 'Crime':
                variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft'), ('violent crime rate', 'Violent Crime Rate'), \
                    ('murder and nonnegligent manslaughter rate', \
                      'Murder and Nonnegligent Manslaughter Rate',) \
                    ('rape rate', 'Rape Rate'), ('robbery rate', 'Robbery Rate'), \
                    ('aggravated assault rate', 'Aggravated Assault Rate'), \
                    ('property crime rate', 'Property Crime Rate'), \
                    ('burglary rate', 'Burglary Rate'), \
                    ('larceny-theft rate', 'Larceny-Theft Rate'), \
                    ('motor vehicle theft rate', 'Motor Vehicle Theft Rate')]
              else:
                variables = [('total arrests', 'Total Arrests'), \
                            ('violent crime index', 'Violent Crime Index'), \
                            ('murder and nonnegligent manslaughter rate', \
                              'Murder and Nonnegligent Manslaughter'), \
                            ('rape', 'Rape'), ('robbery', 'Robbery'), \
                            ('aggravated assault', 'Aggravated Assault'), \
                            ('property crime index', 'Property Crime Index'), \
                            ('burglary', 'Burglary'), ('larceny-theft', \
                            'Larceny-Theft'), ('motor vehicle theft', \
                            'Motor Vehicle Theft'), ('arson', 'Arson'), \
                            ('forgery and counterfeiting', 'Forgery and Counterfeiting'), \
                            ('fraud', 'Fraud'), ('embezzlement', 'Embezzlement'), \
                            ('vandalism', 'Vandalism'), ('weapons', 'Weapons'), \
                            ('prostitution', 'Prostitution'), ('sex offenses', \
                            'Sex Offenses'), ('drug abuse violations', \
                            'Drug Abuse Violations'), ('driving under the influence', \
                            'Driving Under the Influence'), ('gambling', 'Gambling'), \
                            ('liquor laws', 'Liquor Laws'), ('drunkenness', \
                            'Drunkenness'), ('disorderly conduct', \
                            'Disorderly Conduct'), ('vagrancy', 'Vagrancy'), \
                            ('curfew and loitering', 'Curfew and Loitering'), \
                            ('runaways', 'Runaways')]
              self.fields['variable_2'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=variables))
            elif loc_type == 'State':
              variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft'), ('violent crime rate', 'Violent Crime Rate'), \
                    ('murder and nonnegligent manslaughter rate', \
                      'Murder and Nonnegligent Manslaughter Rate',) \
                    ('rape rate', 'Rape Rate'), ('robbery rate', 'Robbery Rate'), \
                    ('aggravated assault rate', 'Aggravated Assault Rate'), \
                    ('property crime rate', 'Property Crime Rate'), \
                    ('burglary rate', 'Burglary Rate'), \
                    ('larceny-theft rate', 'Larceny-Theft Rate'), \
                    ('motor vehicle theft rate', 'Motor Vehicle Theft Rate')]
              self.fields['variable_2'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=variables))
            elif loc_type == 'City':
              if var_type == 'Crime':
                variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft'), ('violent crime rate', 'Violent Crime Rate'), \
                    ('murder and nonnegligent manslaughter rate', \
                      'Murder and Nonnegligent Manslaughter Rate',) \
                    ('rape rate', 'Rape Rate'), ('robbery rate', 'Robbery Rate'), \
                    ('aggravated assault rate', 'Aggravated Assault Rate'), \
                    ('property crime rate', 'Property Crime Rate'), \
                    ('burglary rate', 'Burglary Rate'), \
                    ('larceny-theft rate', 'Larceny-Theft Rate'), \
                    ('motor vehicle theft rate', 'Motor Vehicle Theft Rate')]
              else:
                variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft')]
              self.fields['variable_2'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=variables))
          except (ValueError, TypeError):
            pass

class VariableChoices2(forms.ModelForm):
    class Meta:
        model = models.VariableChoices2
        fields = ['location_type_2', 'location_2', 'variable_type_2', 'variable_2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location_type_2'] = forms.CharField(label="Location Type", \
                    widget=forms.Select(choices=[('country', 'Country'), \
                            ('state', 'State'), ('city', 'City')]))
        self.fields['location_2'] = forms.CharField(label="Location", \
                    widget=forms.Select(choices=[]))
        self.fields['variable_type_2'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[]))
        self.fields['variable_2'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=[]))

        if 'location_type_2' in self.data:
          try:
            loc_type = self.data.get('location_type_2')
            if loc_type == 'Country':
              self.fields['location_2'] = forms.CharField(label="Location", \
                    widget=forms.Select(choices=[('us', 'United States')]))
              self.fields['variable_type_2'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[('us_arrest', 'Arrest'), \
                            ('us_crime', 'Crime')]))
            elif loc_type == 'State':
              self.fields['location_2']= forms.CharField(label="Location", \
                    widget=forms.Select(choices=states))
              self.fields['variable_type_2'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[('state_crime', 'Crime')]))
            elif loc_type == 'City':
              self.fields['location_2']= forms.CharField(label="Location", \
                    widget=forms.Select(choices=get_cities()))
              self.fields['variable_type_2'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[('city_arrest', 'Arrest'), \
                            ('city_crime', 'Crime')]))
          except (ValueError, TypeError):
            pass

        if 'variable_type_2' in self.data:
          try:
            loc_type = self.data.get('location_type_2')
            var_type = self.data.get('variable_type_2')
            loc_1 = self.data.get('location_1')
            loc_2 = self.data.get('location_2')
            if loc_type == 'Country':
              if var_type == 'Crime':
                variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft'), ('violent crime rate', 'Violent Crime Rate'), \
                    ('murder and nonnegligent manslaughter rate', \
                      'Murder and Nonnegligent Manslaughter Rate',) \
                    ('rape rate', 'Rape Rate'), ('robbery rate', 'Robbery Rate'), \
                    ('aggravated assault rate', 'Aggravated Assault Rate'), \
                    ('property crime rate', 'Property Crime Rate'), \
                    ('burglary rate', 'Burglary Rate'), \
                    ('larceny-theft rate', 'Larceny-Theft Rate'), \
                    ('motor vehicle theft rate', 'Motor Vehicle Theft Rate')]
              else:
                variables = [('total arrests', 'Total Arrests'), \
                            ('violent crime index', 'Violent Crime Index'), \
                            ('murder and nonnegligent manslaughter rate', \
                              'Murder and Nonnegligent Manslaughter'), \
                            ('rape', 'Rape'), ('robbery', 'Robbery'), \
                            ('aggravated assault', 'Aggravated Assault'), \
                            ('property crime index', 'Property Crime Index'), \
                            ('burglary', 'Burglary'), ('larceny-theft', \
                            'Larceny-Theft'), ('motor vehicle theft', \
                            'Motor Vehicle Theft'), ('arson', 'Arson'), \
                            ('forgery and counterfeiting', 'Forgery and Counterfeiting'), \
                            ('fraud', 'Fraud'), ('embezzlement', 'Embezzlement'), \
                            ('vandalism', 'Vandalism'), ('weapons', 'Weapons'), \
                            ('prostitution', 'Prostitution'), ('sex offenses', \
                            'Sex Offenses'), ('drug abuse violations', \
                            'Drug Abuse Violations'), ('driving under the influence', \
                            'Driving Under the Influence'), ('gambling', 'Gambling'), \
                            ('liquor laws', 'Liquor Laws'), ('drunkenness', \
                            'Drunkenness'), ('disorderly conduct', \
                            'Disorderly Conduct'), ('vagrancy', 'Vagrancy'), \
                            ('curfew and loitering', 'Curfew and Loitering'), \
                            ('runaways', 'Runaways')]
              if loc_1 == loc_2:
                variables = [('time', 'Time')] + variables
              self.fields['variable_2'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=variables))
            elif loc_type == 'State':
              variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft'), ('violent crime rate', 'Violent Crime Rate'), \
                    ('murder and nonnegligent manslaughter rate', \
                      'Murder and Nonnegligent Manslaughter Rate',) \
                    ('rape rate', 'Rape Rate'), ('robbery rate', 'Robbery Rate'), \
                    ('aggravated assault rate', 'Aggravated Assault Rate'), \
                    ('property crime rate', 'Property Crime Rate'), \
                    ('burglary rate', 'Burglary Rate'), \
                    ('larceny-theft rate', 'Larceny-Theft Rate'), \
                    ('motor vehicle theft rate', 'Motor Vehicle Theft Rate')]
              if loc_1 == loc_2:
                variables = [('time', 'Time')] + variables
              self.fields['variable_2'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=variables))
            elif loc_type == 'City':
              if var_type == 'Crime':
                variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft'), ('violent crime rate', 'Violent Crime Rate'), \
                    ('murder and nonnegligent manslaughter rate', \
                      'Murder and Nonnegligent Manslaughter Rate',) \
                    ('rape rate', 'Rape Rate'), ('robbery rate', 'Robbery Rate'), \
                    ('aggravated assault rate', 'Aggravated Assault Rate'), \
                    ('property crime rate', 'Property Crime Rate'), \
                    ('burglary rate', 'Burglary Rate'), \
                    ('larceny-theft rate', 'Larceny-Theft Rate'), \
                    ('motor vehicle theft rate', 'Motor Vehicle Theft Rate')]
              else:
                variables = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft')]
              if loc_1 == loc_2:
                variables = [('time', 'Time')] + variables
              self.fields['variable_2'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=variables))
          except (ValueError, TypeError):
            pass


class NextPageForm(forms.ModelForm):
    class Meta:
        model = models.NextPage
        fields = ['variable_type_1', 'location_type_1', 'variable_1', \
                  'location_1', 'variable_type_2', 'location_type_2', \
                  'variable_2', 'location_2']
