from django import forms
from django.forms import ModelForm
from . import models
from .models import LocationType1, Location1, VariableType1, VariableChoices1
from smart_selects.db_fields import ChainedForeignKey
import sqlite3


years = [('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'),
            ('2005', '2005')]

class YearForm(forms.Form):
    year_type = forms.CharField(label="Year", \
                    widget=forms.Select(choices=years))


class VariableChoices1(forms.ModelForm):
    class Meta:
        model = models.VariableChoices1
        fields = ['location_type_1', 'location_1', 'variable_type_1', 'variable_1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'] = forms.CharField(label="Year", \
                    widget=forms.Select(choices=years))
        self.fields['location_1'] = forms.CharField(label="Location", \
                    widget=forms.Select(choices=[]))
        self.fields['variable_type_1'] = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[]))
        self.fields['variable_1'] = forms.CharField(label="Variable", \
                    widget=forms.Select(choices=[]))
        print('location_type_1' in self.data)

        if 'location_type_1' in self.data:
          print(True)
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
