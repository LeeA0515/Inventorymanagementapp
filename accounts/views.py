from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Message

def home(request):
    messages = Message.objects
    return render(request, 'accounts/home.html', {'messages': messages})

def about(request):
    return render(request, 'accounts/about.html')

def register(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/register.html', {'error':'This username is not available'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')   
        else:
            return render(request, 'accounts/register.html', {'error':'Passwords do not match'})
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password does not match.'})
    else:
        return render(request, 'accounts/login.html')    
    
def logoff(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

@login_required
def createpost(request):
    if request.method == 'POST':
        if request.POST['topic'] and request.POST['body']:
            message = Message()
            message.topic = request.POST['topic']
            message.body = request.POST['body']
            message.date = timezone.datetime.now()
            message.poster = request.user
            message.save()
            return redirect('home')
        else:
            return render(request, 'accounts/createpost.html', {'error':'Please enter a topic and a message'})
    else:
        return render(request, 'accounts/createpost.html')
