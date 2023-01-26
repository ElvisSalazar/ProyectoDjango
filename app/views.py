from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

# Create your views here.
def presentation(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return redirect('session')
            except:
                return render(request, 'registration.html',{
                    'form': UserCreationForm,
                    'error': 'Username Already exist'
                })

        return render(request, 'registration.html',{
                    'form': UserCreationForm,
                    'error': 'Password do not match'
                })

def signout(request):
    logout(request)
    return redirect('presentation')

def contact(request):
    return render(request,'contacto.html')

def buy(request):
    return render(request,'ventas.html')

def propiety(request):
    return render(request, 'propiedad.html')

def iniciosesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password =password  )

        if user is None:
            return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'invalid username or password'
        })

        login(request, user)
        return redirect('presentation')