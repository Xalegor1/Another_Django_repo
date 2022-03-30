import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = [
        {   
            'breath': 'Breath of the Sun', 
            'location':'Paris', 
            'slug':'a-first-breath'
        },
        {
            'breath': 'Water style: Shark breath', 
            'location': 'Ufa',
            'slug':'a-second-breath'
         }
    ]
    return render(request, 'core/index.html', {
        'show_breath': True,
        'breaths': context
    })
