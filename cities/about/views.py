from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import date
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        fname =  request.POST.get('fname')
        print(username)
        lname =  request.POST.get('lname')
        email =  request.POST.get('email')
        pass1 =  request.POST.get('pass1')
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        if myuser is None:
            return redirect('/signup')
        
        else:
            myuser.save()
    
            return redirect('/signin')

    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request,user)
            return redirect('/postcity')
        else:
            return redirect('/signin')
            
    return render(request,'signin.html')

def postcity(request):

    # user = request.user
    
    if request.user.is_anonymous:
        return redirect('/signin')

    if request.method == 'POST':
        details = Postfrom(request.POST)

        if details.is_valid():    
            d = Postfrom(request.POST)
            post = d.save()
            post.save()
            return redirect('/cities')
        
        else :
            return render(request, "cityform.html", {'form':details})
    else:
        form = Postfrom({'name':"name of the city you visited",'geography':"Demographics of the city",'history':"History of the city",'culture' : "Cultural Attraction",'language':"Languages Spoken",'infrastructure' : "Infrastructural Development", 'tourist':"Places to visit"})
        return render(request,'cityform.html',{'form':form})
    

        

def signout(request):
    logout(request)
    return redirect('/')

def viewcity(request):
    passed_list : dict[str:list] = {"list" : []}
    for obj in Cities.objects.all():
        context = {
            'id' : obj.id,
            'name' : obj.name,
            'geography' : obj.geography,
            'history' : obj.history,
            'culture' : obj.culture,
            'language' : obj.language,
            'infrastructure' : obj.infrastructure,
            'tourist_spots' : obj.tourist_spots
        }
        passed_list["list"].append(context)

    print('Passed',  len(passed_list['list']))
    return render(request, 'viewcity.html', passed_list) 
