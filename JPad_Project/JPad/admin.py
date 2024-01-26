from django.contrib import admin
from .models import Profile
from .models import Todo
from .models import Debt


# Register your models here.
admin.site.register(Profile)
admin.site.register(Todo)
admin.site.register(Debt)