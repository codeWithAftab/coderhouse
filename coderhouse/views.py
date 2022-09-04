from asyncio import constants
from multiprocessing import context
from django.shortcuts import render,redirect
from coderhouse.models import Profile,myProjects
from django.templatetags.static import static
# Create your views here.


def home(request):
    projects = myProjects.objects.all()
    owner = Profile.objects.get(name="Aftab")

    print(projects)
    context = {
        "projects":projects,
        "owner":owner,
        "resume":"assets/resume.pdf"
    }
    print()
    print(context)
    return render(request,"index.html",context)