from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    items_list = Item.objects.all()
    return HttpResponse(items_list)

def item(request):
    return HttpResponse("This is one of the food items on our menu")
