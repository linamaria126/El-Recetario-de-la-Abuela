from rest_framework.viewsets import ModelViewSet
from recetas.models import Receta
from recetas.api.serializers import RecetaSerializer
# Añadir los permisos
from ingredientes.api.permissions import IsAdminReadOnly

class RecetaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = RecetaSerializer
    queryset = Receta.objects.all()
    