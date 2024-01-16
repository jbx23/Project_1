# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']  # Include default fields as needed

class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password'] 