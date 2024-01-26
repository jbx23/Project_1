# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Profile
from django.contrib.auth import get_user_model, login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
def initial_landing(request):
    return render(request, 'initial_landing.html')
def contact_us(request):
    return render(request, 'contactUs.html')
def register(request):
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        age=request.POST['age']
        password=request.POST['password']
        password2=request.POST['password2']

        age=int(age) if age.strip() else None
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist!')
                return redirect('register')
            else:
                user=User.objects.create_user(username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                user_model=User.objects.get(username=user)
                new_profile=Profile.objects.create(user=user_model, username=username, first_name=firstname, last_name=lastname, email=email, age=age, password=password)
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
                messages.success(request, f"Hello {user.username}! you are logged in")
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
from .models import Todo
from .forms import TodoForm

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    # Assuming you have a Profile object for the logged-in user
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html',{'profile':profile})

def todo_list(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    form = TodoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo')  # Redirect to the same page after form submission
    else:
        form = TodoForm()

    tasks_todo = Todo.objects.filter(user=request.user, is_done=False)
    tasks_done = Todo.objects.filter(user=request.user, is_done=True)

    return render(request, 'todo.html', {'tasks_todo': tasks_todo, 'tasks_done': tasks_done, 'form': form})

from django.http import JsonResponse


def move_task(request, task_id):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    if request.method == 'POST':
        task = Todo.objects.get(pk=task_id)
        from_list = request.POST.get('from_list')
        to_list = request.POST.get('to_list')
        print(f'Task ID: {task_id}, From List: {from_list}, To List: {to_list}, is_done: {task.is_done}')
        if from_list == 'todo' and to_list == 'done':
            task.is_done = True
        elif from_list == 'done' and to_list == 'todo':
            task.is_done = False
        else:
            return JsonResponse({'error': 'Invalid request.'}, status=400)

        task.save()
        return JsonResponse({'message': 'Task moved.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def reset_tasks(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    # Delete all tasks for the logged-in user
    Todo.objects.filter(user=request.user).delete()

    return redirect('todo')  # Redirect back to the todo list page

from .models import Debt
from .forms import DebtForm

def debt_tracker(request):   
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in 
    form = DebtForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_debt = form.save(commit=False)
            new_debt.user = request.user
            new_debt.save()
            return redirect('debt_tracker')  
    else:
        form = DebtForm()
    user_debts = Debt.objects.filter(user=request.user)

    return render(request, 'debtTracker.html', {'user_debts': user_debts, 'form': form})

def reset_debt(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    # Delete all tasks for the logged-in user
    Debt.objects.filter(user=request.user).delete()

    return redirect('debtTracker')  # Redirect back to the debt tracker page


from .forms import EditProfileForm
def edit_profile(request):
    """
    Allows the logged-in user to edit their own profile.
    Handles both the GET and POST methods. 
    """
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    form = EditProfileForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if new_password and new_password == confirm_password:
                user.set_password(new_password)
            user.save()
            if new_password:
                update_session_auth_hash(request, user)  # Updates the session hash to keep the user authenticated

            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'editProfile.html', {'form': form})


from .forms import EditDebtForm
def edit_debt(request, debt_id):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    debt = get_object_or_404(Debt, id=debt_id, user=request.user)
    print(debt)
    form = EditDebtForm(request.POST, instance=debt)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('debt_tracker')
    else:
        form = EditDebtForm(instance=debt)

    return render(request, 'editDebt.html', {'form': form})

def remove_debt(request, debt_id):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login to Acess This page!')
        return redirect('login')  # Redirect to login if user is not logged in
    debt = get_object_or_404(Debt, id=debt_id, user=request.user)
    if debt.user != request.user:
        # Redirect or handle unauthorized access
        return redirect('debt_tracker')
    debt.delete()
    return redirect('debt_tracker')
def gpa_converter(request):
    return render(request, 'GPAConverter.html')
def currency_converter(request):
    return render(request, 'CurrencyConverter.html')
def home(request):
    return render(request, 'home.html')