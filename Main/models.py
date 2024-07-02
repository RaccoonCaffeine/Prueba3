from django.db import models

# Create your models here.
class Navbar(models.Model):
    id_nav = models.CharField(max_length=25,db_column="idNav", primary_key=True)
    nombre_nav = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.nombre_nav
    
class Quienes(models.Model):
    id_quienes = models.CharField(max_length=25, db_column="idQuienes", primary_key=True)
    titulo_quienes = models.CharField(max_length=25, blank=False, null=False, default='Default')
    descripcion_quienes = models.TextField(blank=False)
 
    def __str__(self):
        return self.titulo_quienes


class Servicios(models.Model):
    id_servicios = models.AutoField(db_column="idServicios", primary_key=True)
    titulo_servicios = models.CharField(max_length=70, blank=False, null=False)
    descripcion_servicios = models.TextField(blank=False, null=False)
    imagen_servicios = models.ImageField(upload_to='img/servicios/', blank=False, null=False)

    def __str__(self):
        return self.titulo_servicios