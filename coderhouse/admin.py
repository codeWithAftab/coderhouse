import profile
from django.contrib import admin
from .models import Profile, myProjects

# Register your models here.
admin.site.register(myProjects)
admin.site.register(Profile)