from django.urls import path
from . import views
from.views import Index

urlpatterns = [    
    # Profile and user-related paths
    path('', Index.as_view(), name='profile'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]