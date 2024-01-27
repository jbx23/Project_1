from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [    
    path('', views.initial_landing, name='initial_landing'),
    path('register/',views.register,name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout', LogoutView.as_view(template_name='initial_landing.html'), name='logout'),
    path('profile/', views.profile, name= 'profile'),
    path('home/', views.home, name='home'),
    path('todo/', views.todo_list, name='todo'),
    path('move_task/<int:task_id>/', views.move_task, name='move_task'),
    path('reset_tasks/', views.reset_tasks, name='reset_tasks'),
    path('debt_tracker/', views.debt_tracker, name='debt_tracker'),
    path('reset_debt/', views.reset_debt, name='reset_debt'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_debt/<int:debt_id>', views.edit_debt, name='edit_debt'),
    path('remove_debt/<int:debt_id>/', views.remove_debt, name='remove_debt'),
    path('gpa_converter/', views.gpa_converter, name='gpa_converter'),
    path('currency_converter/',views.currency_converter, name='currency_converter'),
    path('contact_us/', views.contact_us, name='contact'),
]