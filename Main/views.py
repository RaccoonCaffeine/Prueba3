from django.shortcuts import render
from .models import Navbar,Quienes,Servicios

def index(request):
    titulo = "Home"
    navbars = Navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo}
    return render(request, 'home.html', context)

def quienes(request):
    titulo = 'Quienes Somos'
    quienes = Quienes.objects.all()
    navbars = Navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'quienes': quienes}
    return render(request,'quienessomos.html',context)

def servicios(request):
    titulo = 'Servicios'
    servicios = Servicios.objects.all()
    navbars = Navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'servicios': servicios}
    return render(request,'servicios.html',context)