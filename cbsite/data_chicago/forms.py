from django import forms
from django.forms import ModelForm
from . import models
from .models import LocationType1, Location1, VariableType1, VariableChoices1
from smart_selects.db_fields import ChainedForeignKey
import sqlite3


years = [('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'),
            ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'),
            ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'),
            ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'),
            ('2017', '2017'), ('2018', '2018')]

crimes = [('violent crime total', 'Violent Crime Total'), \
                      ('murder and nonnegligent manslaughter', \
                        'Murder and Nonnegligent Manslaughter'), \
                    ('rape', 'Rape'), ('robbery', 'Robbery'), ('aggravated assault', \
                      'Aggravated Assault'), ('property crime total', \
                      'Property Crime Total'), ('burglary', 'Burglary'), \
                    ('larceny-theft', 'Larceny-Theft'), ('motor vehicle theft', \
                      'Motor Vehicle Theft'), ('violent crime rate', 'Violent Crime Rate'), \
                    ('murder and nonnegligent manslaughter rate', \
                      'Murder and Nonnegligent Manslaughter Rate'), \
                    ('rape rate', 'Rape Rate'), ('robbery rate', 'Robbery Rate'), \
                    ('aggravated assault rate', 'Aggravated Assault Rate'), \
                    ('property crime rate', 'Property Crime Rate'), \
                    ('burglary rate', 'Burglary Rate'), \
                    ('larceny-theft rate', 'Larceny-Theft Rate'), \
                    ('motor vehicle theft rate', 'Motor Vehicle Theft Rate')]

tooltips = [('yes', 'yes'), ('no', 'no')]

class FormThing(forms.ModelForm):
    class Meta:
        fields = ['years', 'crimes', 'tooltips', 'data_points']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'] = forms.CharField(label="Year", \
                    widget=forms.Select(choices=years))
        self.fields['crime type'] = forms.CharField(label="Crime type", \
                    widget=forms.Select(choices=crimes))
        self.fields['tooltips'] = forms.CharField(label="Tooltips?", \
                    widget=forms.Select(choices=tooltips))
        self.fields['data_points'] = forms.CharField(label="How many data points?", \
                    widget=forms.Select(choices=[]))


