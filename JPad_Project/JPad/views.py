# myapp/views.py
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .models import Profile

class Index(View):
    def get(self,request):
        return render(request,'profile.html')
    
def register(request):
    if request.method =='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist!')
                return redirect('register/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist!')
                return redirect('register/')
            else:
                user=User.objects.create_user(name=name,lastname=lastname,username=username,email=email,password=password)
                user.save()
                user_model=user.objects.get(username=username)
                new_profile=Profile.objects.create(user=user.model, id_user=user_model.id)
                new_profile.save()
                return redirect('login/')
        else:
            messages.info(request,'password do not match')
            return redirect('register/')
    else:
        return render (request,'register.html')
    
def login(request):
    return render (request,'login.html')
    