from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
User=get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username=models.TextField()
    first_name=models.TextField()
    last_name=models.TextField()
    email=models.EmailField()
    age=models.IntegerField(blank=True, null=True)
    password=models.TextField()

    def __str__(self):
        return self.user

class Todo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return self.user
    
class Debt(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.name}: ${self.amount}"


    
