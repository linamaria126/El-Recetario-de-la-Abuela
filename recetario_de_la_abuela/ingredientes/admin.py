from django.contrib import admin
from ingredientes.models import Ingrediente

# Register your models here.

@admin.register(Ingrediente)

class IngredienteAdmin(admin.ModelAdmin):
    pass
