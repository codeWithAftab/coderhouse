from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('students/', views.student, name="students_proj"),
    path('students/download22', views.myview, name="download"),
]
