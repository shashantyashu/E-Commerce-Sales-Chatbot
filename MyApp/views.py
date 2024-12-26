from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from MyApp.models import Product
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products } )

def show(request, id):
    if request.user.is_anonymous:
        return redirect("/login")
    products = Product.objects.all()
    context = {'id': id}
    data = {
        
        'context': context,
        'product': products,
    }
    
    return render(request, 'show.html', data)

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/explore')
    else:
        initial_data = {'username':"", 'password1':"", 'password2':""}
        
        
        form = UserCreationForm(initial=initial_data)
        print(form)
    return render(request, 'auth/register.html',{'form':form})


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
           
            login(request, user)
            return redirect("/explore")
        else:
            
            return render(request, 'login.html')    
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
