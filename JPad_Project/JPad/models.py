from django.db import models
from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()

class Profile(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.TextField()
    last_name=models.TextField()
    location=models.CharField(max_length=100, blank=True)
    age=models.IntegerField()

    def __str__(self):
        return self.username


    
