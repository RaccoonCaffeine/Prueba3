from django.shortcuts import render
from .models import Navbar

def index(request):
    navbars = Navbar.objects.all()
    context = {'navbar': navbars}
    return render(request, 'home.html', context)

def quienes(request):
    navbars = Navbar.objects.all()
    context = {'navbar': navbars}
    return render(request,'quienessomos.html',context)

def servicios(request):
    navbars = Navbar.objects.all()
    context = {'navbar': navbars}
    return render(request,'servicios.html',context)