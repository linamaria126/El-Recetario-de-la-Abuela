from rest_framework.routers import DefaultRouter
from ingredientes.api.views import IngredienteApiViewSet


router_ingredientes = DefaultRouter()
router_ingredientes.register(prefix='ingredientes', basename='ingredientes', viewset=IngredienteApiViewSet)
