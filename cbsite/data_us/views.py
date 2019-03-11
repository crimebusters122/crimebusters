from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .forms import LocationTypeForm

def loc_type(request):
    if request.method == 'POST':
        form = LocationTypeForm(request.POST)
        return HttpResponseRedirect('')
    else:
        form = LocationTypeForm()
    return render(request, 'data_us/loctype.html', {'form': form})
