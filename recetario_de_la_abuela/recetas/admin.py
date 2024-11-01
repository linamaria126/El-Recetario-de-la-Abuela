from django.contrib import admin
from recetas.models import Receta

# Register your models here.
# Enviar  al panel de administración el modelo
@admin.register(Receta)

class RecetaAdmin(admin.ModelAdmin):
    list_display = [ 'nombre_receta', 'descripcion', 'mostrar_imagen']
    