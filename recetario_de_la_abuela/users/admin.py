from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)
# Register your models here.
class UserAdmin(BaseUserAdmin):
    pass

admin.site.site_header = 'Recetario de la abuela'
admin.site.index_title = 'Panel de control de mi sitio'
admin.site.site_title = 'Recetario de la abuela'