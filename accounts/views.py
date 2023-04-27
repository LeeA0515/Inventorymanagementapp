from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def home(request):
    return render(request, 'accounts/home.html')

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