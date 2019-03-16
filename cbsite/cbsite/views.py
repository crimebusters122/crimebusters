from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def homepg(request):
    return render(request, 'cbsite/cb.html')