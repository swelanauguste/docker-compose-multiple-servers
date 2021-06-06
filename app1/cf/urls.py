from django.shortcuts import render
from django.contrib import admin
from django.urls import path

def index(request):
    return render(request, 'index.html', {'name':'Swelan Auguste app1'})

urlpatterns = [
    path("", index),
    path('admin/', admin.site.urls),
]
