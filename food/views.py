from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.

def index(request):
    items_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    #the context passed into the template is the data from the database
    context = {
        'items_list':items_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html', context)

def item(request):
    return HttpResponse("This is one of the food items on our menu")

def detail(request, item_id):
    menu_item = Item.objects.get(pk=item_id)
    context = {
        "item":menu_item,
    }
    return render(request, 'food/detail.html', context)
    # return HttpResponse(template.render(context, request))

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,"food/item-form.html",{"form":form})
