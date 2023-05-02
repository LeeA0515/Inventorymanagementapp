from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('additem/', views.additem, name='additem'),
    path('itemlist/', views.itemlist, name='itemlist'),
    path('requestitem/', views.requestitem, name='requestitem'),
    path('management/', views.management, name='management'),
    path('<int:item_id>/changeitem', views.changeitem, name='changeitem')
]