from distutils.command.upload import upload
from statistics import mode
from django.db import models


# Create your models here.
class myProjects(models.Model):
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to="images/", default="")
    desc = models.CharField(max_length=322,default="")
    url = models.CharField(max_length=1222,default="#")

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to="profile/")
    bio = models.CharField(max_length=3222)
    phone = models.CharField(max_length=3222)
    email = models.CharField(max_length=3222)
    address = models.CharField(max_length=3222)
    facebook = models.CharField(max_length=122,default="#")
    instagram = models.CharField(max_length=12223,default="#")
    github = models.CharField(max_length=12223,default="#")
    linkdin = models.CharField(max_length=12223,default="#")
    
    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=122,default="",null=True,blank=True)
    eno = models.CharField(max_length=122,default="",null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    proj_title = models.CharField(max_length=200,default="",null=True,blank=True)
    technology = models.CharField(max_length=122,default="",null=True,blank=True)
    frontend_tech = models.TextField(default="",null=True,blank=True)
    backend_tech = models.TextField(default="",null=True,blank=True)
    proj_desc = models.TextField(default="",null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)

       
    def __str__(self) -> str:
        return f"{self.name} ({str(self.eno)})"
