from django import forms
from .models import Data

class DataForm(forms.Form):
    data = forms.CharField(label="Select Data", \
            widget=forms.Select(choices=[('chicago', 'Chicago'), \
                    ('usa', 'United States')]))
