"""
URL configuration for recetario_de_la_abuela project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# importación API's propias
from recetas.api.router import router_recetas
from ingredientes.api.router import router_ingredientes
from favoritos.api.router import router_favoritos
from recetaIngredientes.api.router import router_recetaIngredientes


schema_view = get_schema_view(
   openapi.Info(
      title="Recetario API",
      default_version='v1',
      description="Documentación Api del proyecto Recetario de la abuela",
      terms_of_service="",
      contact=openapi.Contact(email="linamaria126@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_recetas.urls)),
    path('api/', include(router_ingredientes.urls)),
    path('api/', include(router_favoritos.urls)),
    path('api/', include(router_recetaIngredientes.urls)),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

