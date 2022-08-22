from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    first = '<h1>first project</h1>'
    return HttpResponse(first)