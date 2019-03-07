from django.shortcuts import render
from django.http import HttpResponse


from . import models
from .forms import LocationTypeForm

def get_loc_type(request):
    if request.method == 'POST':
        form = LocationTypeForm(request.POST)
        return HttpResponseRedirect('/thanks/')
    else:
        form = LocationTypeForm()
    return render(request, 'homepg/loctype.html', {'form': form})


