from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def item(request):
    return HttpResponse("This is one of the food items on our menu")
