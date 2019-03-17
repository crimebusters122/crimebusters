from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from .forms import DataForm

def get_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect('')
    else:
        form = DataForm()
    return render(request, 'home/homepage.html', {'form': form})