from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Equipment
import operator

@login_required
def addequip(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['ecn'] and request.POST['ecndate']:
            equip = Equipment()
            equip.name = request.POST['name']
            equip.ecn = request.POST['ecn']
            equip.ecndate = request.POST['ecndate']
            equip.account = request.user
            equip.save()
            return redirect('/equipment/equiplist')
        else:
            return render(request, 'equipment/addequip.html', {'error': "All fields required to submit."})
    else:
        return render(request, 'equipment/addequip.html')    
# Create your views here.

@login_required
def changeequip(request,equip_id):
    equip = Equipment.objects.get(id=equip_id)
    if request.method == 'POST':
        if request.POST['name'] and request.POST['ecn'] and request.POST['ecndate']:
            equip.name = request.POST['name']
            equip.ecn = request.POST['ecn']
            equip.ecndate = request.POST['ecndate']
            equip.save()
            return redirect('/equipment/equiplist')
        else:
            return render(request, 'equipment/changeequip.html', {'equip':equip, 'error':'please enter a value in all fields'})
    else:
        return render (request, 'equipment/changeequip.html', {'equip':equip})
    
def equiplist(request):
    equip = Equipment.objects

    return render(request, 'equipment/equiplist.html', {'equip':equip})    
