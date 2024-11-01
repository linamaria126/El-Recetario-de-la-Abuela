from rest_framework.viewsets import ModelViewSet
from recetaIngredientes.models import  RecetaIngrediente
from recetaIngredientes.api.serializers import RecetaIngredienteSerializer
# Añadir los permisos
from ingredientes.api.permissions import IsAdminReadOnly

class RecetaIngredienteApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = RecetaIngredienteSerializer
    queryset = RecetaIngrediente.objects.all()