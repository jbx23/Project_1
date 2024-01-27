from django import forms
from .models import Todo
from.models import Debt
from.models import Profile
from django.contrib.auth.models import User
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']
class DebtForm(forms.ModelForm):
    class Meta:
        model=Debt
        fields=['name', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
class EditProfileForm(forms.ModelForm):
    """Form for editing profile with optional password change"""
    new_password = forms.CharField(required=False, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
class EditDebtForm(forms.ModelForm):
    class Meta:
        model=Debt
        fields=['name', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }