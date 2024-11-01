from rest_framework.viewsets import ModelViewSet
from ingredientes.models import Ingrediente
from ingredientes.api.serializer import IngredienteSerializer
# Añadir los permisos
from ingredientes.api.permissions import IsAdminReadOnly


class IngredienteApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()
