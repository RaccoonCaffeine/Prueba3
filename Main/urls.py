from django.urls import path, include
from . import views as main

urlpatterns=[
    path('',main.index,name="index"),
    path('index/',main.index,name="index"),
    path('quienes/',main.quienes,name="quienes"),
    path('servicios/',main.servicios,name="servicios")
]
