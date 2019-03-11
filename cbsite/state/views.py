from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .forms import VariableTypeForm

def var_type(request):
    if request.method == 'POST':
        form = VariableTypeForm(request.POST)
        return HttpResponseRedirect('')
    else:
        form = VariableTypeForm()
    return render(request, 'state/states_vars.html', {'form': form})