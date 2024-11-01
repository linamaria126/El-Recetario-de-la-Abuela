from django.contrib import admin
from recetaIngredientes.models import RecetaIngrediente

# Register your models here.
@admin.register(RecetaIngrediente)

class RecetaIngredienteAdmin(admin.ModelAdmin):
    list_display = ['cantidades', 'id_ingredientes', 'id_recetas']