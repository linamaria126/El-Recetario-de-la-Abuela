from django.db import models
from django.utils.html import format_html

# Create your models here.
class Receta(models.Model):
    id_recetas = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_receta = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=2000)
    porciones = models.IntegerField()
    imagen = models.ImageField(upload_to='recetas/', null=True, max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'RECETAS'

    def mostrar_imagen(self):
        if self.imagen:
            return format_html('<img src= "{}" width = "50" height="50">'.format(self.imagen.url))
        else: 
            return ''
        

    mostrar_imagen.short_description = "Imagen"

    def __str__(self):
        return self.nombre_receta