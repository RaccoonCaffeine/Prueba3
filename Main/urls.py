from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as main

urlpatterns=[
    path('',main.index,name="index"),
    path('index/',main.index,name="index"),
    path('quienes/',main.quienes,name="quienes"),
    path('servicios/',main.servicios,name="servicios")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
