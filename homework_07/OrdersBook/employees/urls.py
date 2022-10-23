from django.contrib import admin
from django.urls import path
from .views import index #, details

app_name = "employees"

urlpatterns = [
    path("", index, name="index"),
    #path("<int:pk>", details, name="details"),
]