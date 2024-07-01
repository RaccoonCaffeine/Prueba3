from django.shortcuts import render
from .models import Navbar

def index(request):
    titulo = "Home"
    navbars = Navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo}
    return render(request, 'home.html', context)

def quienes(request):
    titulo = 'Quienes Somos'
    navbars = Navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo}
    return render(request,'quienessomos.html',context)

def servicios(request):
    titulo = 'Servicios'
    navbars = Navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo}
    return render(request,'servicios.html',context)