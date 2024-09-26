from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addequip/', views.addequip, name='addequip'),
    path('equiplist/', views.equiplist, name='equiplist'),
    path('<int:equip_id>/changeequip', views.changeequip, name='changeequip')
]