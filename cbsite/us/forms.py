from django import forms
from .models import VariableType

class VariableTypeForm(forms.Form):
    variable_type = forms.CharField(label="Variable Type", \
                    widget=forms.Select(choices=[('crime', 'Crimes'), \
                            ('arrest', 'Arrests')]))