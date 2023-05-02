from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Item, Request
import operator

#The views for all Item related function and webpages

#function for adding items to list through the web app. This page is not accessible to other users without url
@login_required
def additem(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['referenceId'] and request.POST['quantity']:
            item = Item()
            item.name = request.POST['name']
            item.referenceId = request.POST['referenceId']
            item.quantity = request.POST['quantity']
            item.account = request.user
            item.save()
            return redirect('/items/itemlist')
        else:
            return render(request,'items/additem.html', {'error':'All fields required to submit.'})
    else:
        return render(request, 'items/additem.html')
    
# Much the same as the additem function, but just sends a request to better streamline flow of the sight    
@login_required
def requestitem(request):
    if request.method == 'POST':
        if request.POST['namer'] and request.POST['referenceIdr'] and request.POST['quantityr'] and request.POST['comment']:
            requestI = Request()
            requestI.namer = request.POST['namer']
            requestI.referenceIdr = request.POST['referenceIdr']
            requestI.quantityr = request.POST['quantityr']
            requestI.comment = request.POST['comment']
            requestI.subdate = timezone.datetime.now()
            requestI.completed = False
            requestI.account = request.user
            requestI.save()
            return redirect('/items/itemlist')
        else:
            return render(request, 'items/requestitem.html', {'error':'All fields are required to submit.'})
    else:
        return render(request, 'items/requestitem.html')          
       
        
@login_required
def management(request):
    item = Item.objects
    return render(request, 'items/management.html', {'item':item,})

def changeitem(request,item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        if request.POST['quantity']:
            item.quantity = request.POST['quantity']
            item.save()
            return redirect('/items/management')
        else:
            return render(request, 'items/changeitem.html', {'item':item, 'error':'please enter a valid quantity'})
    else:
        return render(request, 'items/changeitem.html', {'item':item})



#function for itemlist page which also holds the request list
def itemlist(request):
    ritem = Request.objects
    items = Item.objects
    return render(request, 'items/itemlist.html', {'items':items, 'ritem':ritem})