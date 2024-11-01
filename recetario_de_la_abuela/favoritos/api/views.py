from rest_framework.viewsets import ModelViewSet
from favoritos.models import  Favorito
from favoritos.api.serializers import FavoritoSerializer
# Añadir los permisos
from ingredientes.api.permissions import IsAdminReadOnly

class FavoritoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = FavoritoSerializer
    queryset = Favorito.objects.all()