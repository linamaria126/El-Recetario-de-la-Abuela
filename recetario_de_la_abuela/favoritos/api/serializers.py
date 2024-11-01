from rest_framework import serializers
from favoritos.models import Favorito


class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['id_favorito','comensales','user_id', 'id_recetas']
