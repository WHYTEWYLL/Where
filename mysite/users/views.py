from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .forms import UserRegisterForm , New_middlepoint
from .models import Middlepoint, MyUsers , Friends
from src.apicall import *
from django.utils.safestring import SafeString
# Create your views here.

def welcome(request):
    if request.user.is_authenticated:
        users = MyUsers.objects.exclude(id = request.user.id)
        form = New_middlepoint(request.POST or None) 
        #friends = Friends.objects.all()        
        if form.is_valid():
            form.instance.user = request.user
            form.instance.middle_points,form.instance.infomarti,form.instance.point_1,form.instance.point_2,nuevo_medio = (my_api_call(form.instance.point_1,form.instance.point_2,tipo =form.instance.type_of_point))
            nuevosdatos =  {"nuevo_point1" :form.instance.point_1 ,"nuevo_point2" : form.instance.point_2 ,"punto_medio": nuevo_medio}
            form.save()
            return render(request, "users/welcome.html",{'form': form,'users':users,"nuevosdatos":nuevosdatos})
        return render(request, "users/welcome.html",{'form': form,'users':users})
    return redirect("/")    

def register(request):
    form= UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "users/register.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "users/login.html",{'form': form})

def logout(request):
    do_logout(request)
    return redirect('/')