from django.db import models

# Create your models here.
class Navbar(models.Model):
    id_nav = models.CharField(max_length=25,db_column="idNav", primary_key=True)
    nombre_nav = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.nombre_nav