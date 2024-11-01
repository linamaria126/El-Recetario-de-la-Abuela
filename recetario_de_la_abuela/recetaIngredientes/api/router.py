from rest_framework.routers import DefaultRouter
from recetaIngredientes.api.views import RecetaIngredienteApiViewSet

router_recetaIngredientes = DefaultRouter()
router_recetaIngredientes.register(prefix='recetaIngredientes', basename='recetaIngredientes', viewset=RecetaIngredienteApiViewSet)