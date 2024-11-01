from rest_framework.routers import DefaultRouter
from favoritos.api.views import FavoritoApiViewSet


router_favoritos = DefaultRouter()
router_favoritos.register(prefix='favoritos', basename='favoritos', viewset=FavoritoApiViewSet)
