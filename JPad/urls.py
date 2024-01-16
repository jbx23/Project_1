# myapp/urls.py
from django.urls import path
from .views import register, user_login, user_logout, cover, home, todo, GPAConverter, debtTracker, CurrencyConverter

urlpatterns = [
    path('', cover, name='cover'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    path('todo/', todo, name='todo'),
    path('GPAConverter/', GPAConverter, name='GPAConverter'),
    path('debtTracker/', debtTracker, name='debtTracker'),
    path('CurrencyConverter/', CurrencyConverter, name='CurrencyConverter'),
    # Add other paths as needed
]
