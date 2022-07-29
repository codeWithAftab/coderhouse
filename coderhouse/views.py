from multiprocessing import context
from django.shortcuts import render,redirect
from coderhouse.models import Profile,myProjects

# Create your views here.


def home(request):
    projects = myProjects.objects.all()
    owner = Profile.objects.get(name="Aftab")

    print(projects)
    context = {
        "projects":projects,
        "owner":owner
    }
    return render(request,"index.html",context)