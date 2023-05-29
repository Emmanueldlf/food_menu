from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView

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

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items_list'


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

def update_item(request,id):
    item_to_update = Item.objects.get(id=id)
    update_form = ItemForm(request.POST or None, instance=item_to_update)

    if update_form.is_valid():
            update_form.save()
            return redirect('food:index')
    return render(request,"food/item-form.html",{"form":update_form,"item":item_to_update})

def delete_item(request,id):
    item_to_delete = Item.objects.get(id=id)

    if request.method == "POST":
        item_to_delete.delete()
        return redirect("food:index")
    return render(request,"food/item-delete.html",{'item':item_to_delete})
