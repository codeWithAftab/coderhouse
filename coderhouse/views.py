from asyncio import constants
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
from coderhouse.models import Profile,myProjects,Project
from django.templatetags.static import static
from coderhouse.utils import download_csv
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

def student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        eno = request.POST.get("eno")
        phone = request.POST.get("phone")
        title = request.POST.get("title")
        front_tech = request.POST.get("front_tech")
        backend_tech =request.POST.get("backend_tech")
        other_tech =request.POST.get("other_tech")
        desc =request.POST.get("desc")
        p = Project.objects.filter(eno=eno).first()
        iserror = {
            "status":False,
            "info":[]
        }
        if len(name) < 3:
            iserror["status"] = True
            iserror["info"].append("name should be greater than three charcters.")
        if len(eno) < 10:
            iserror["status"] = True
            iserror["info"].append("Your enrollment no is invalid.")
        if len(phone) < 10:
            iserror["status"] = True
            iserror["info"].append("Your mobile no is invalid.")
        if desc == "":
            iserror["status"] = True
            iserror["info"].append("description doesnt null should be in breif..")

        if p:
            iserror["status"] = True
            iserror["info"].append("this enrollment no is already exist..")

        if iserror["status"]:
            return render(request,"students.html",{"errors":iserror["info"]})
        
        else:
            student = Project.objects.create(name=name,eno=eno,phone=phone,proj_title=title,frontend_tech=front_tech,backend_tech=backend_tech,technology=other_tech,proj_desc=desc)
            student.save()
            return render(request,"thanks.html")

    return render(request,"student.html")
def redirect_view(request):
    return redirect("/students/")
def myview(request):
    data = download_csv(Project, request, Project.objects.all())

    return HttpResponse (data, content_type='text/csv')
