from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [    
    # Profile and user-related paths
    path('', views.cover, name='cover'),
    path('register/',views.register,name='register'),
    #path('login/', views.sign_login, name='login'),
    path('login/', views.custom_login, name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name= 'profile'),
]