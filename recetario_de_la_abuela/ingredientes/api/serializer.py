from rest_framework import serializers
from ingredientes.models import Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nombre_ingrediente']