from django.contrib import admin
from django.urls import path
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'name':'Swelan Auguste app2'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),

]
