from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # /food/
    path("", views.index,name="index"),
    # /food/:id
    path("<int:item_id>", views.detail,name="detail"),
    path("item/",views.item,name="item"),
]
