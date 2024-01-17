# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Profile
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def cover(request):
    return render(request, 'cover.html')
    
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
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist!')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=name, last_name=lastname, username=username, email=email, password=password)
                user.save()
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(username=user_model, name=name, last_name=lastname, email=email, age=21)
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request,'password do not match')
            return redirect('register')
    else:
        return render (request,'register.html')
    
def sign_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Change 'home' to the desired URL after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

@login_required    
def profile(request):
    # Assuming you have a Profile object for the logged-in user
    profile = Profile.objects.get(username=request.user)
    return render(request, 'profile.html')


def custom_login(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username}! ready to login?")
                return redirect("profile")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form}
        )