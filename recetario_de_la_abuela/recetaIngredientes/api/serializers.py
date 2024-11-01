from rest_framework import serializers
from recetaIngredientes.models import RecetaIngrediente


class RecetaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaIngrediente
        fields = ['id_contiene','id_recetas','id_ingredientes','cantidades']
