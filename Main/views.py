from django.shortcuts import render
from .models import Navbar

def index(request):
    navbars = Navbar.objects.all()
    context = {'navbar': navbars}
    return render(request, 'home.html', context)
