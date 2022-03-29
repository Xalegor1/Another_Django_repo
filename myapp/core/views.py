import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = [
        {'breath': 'Breath of the Sun'},
        {'breath': 'Water style: Shark breath'}
    ]
    return render(request, 'core/index.html', {
        'show_breath': True,
        'breaths': context
    })
