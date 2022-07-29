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