import profile
from django.contrib import admin
from .models import Profile, myProjects,Project

# Register your models here.
admin.site.register(myProjects)
admin.site.register(Project)
admin.site.register(Profile)