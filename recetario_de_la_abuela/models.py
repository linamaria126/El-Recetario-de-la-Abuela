# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Favoritos(models.Model):
    id = models.IntegerField(primary_key=True)
    comensales = models.IntegerField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    id_recetas = models.ForeignKey('Recetas', models.DO_NOTHING, db_column='id_recetas')

    class Meta:
        managed = False
        db_table = 'FAVORITOS'


class Ingredientes(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre_receta = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'INGREDIENTES'


class RecetaIngredientes(models.Model):
    id_contiene = models.AutoField(db_column='Id_contiene', primary_key=True)  # Field name made lowercase.
    id_recetas = models.ForeignKey('Recetas', models.DO_NOTHING, db_column='Id_recetas')  # Field name made lowercase.
    id_ingredientes = models.ForeignKey(Ingredientes, models.DO_NOTHING, db_column='Id_Ingredientes')  # Field name made lowercase.
    cantidades = models.DecimalField(max_digits=20, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'RECETA-INGREDIENTES'


class Recetas(models.Model):
    id_recetas = models.IntegerField(db_column='Id_recetas', primary_key=True)  # Field name made lowercase.
    nombre_receta = models.CharField(max_length=100)
    descripcion = models.TextField()
    porciones = models.IntegerField()
    imagen = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'RECETAS'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UsersUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user_id', 'group_id'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)

# Ejemplos de tipos de campos de Django para tener como modelos:

class Usuario(models.Model):
    # Campos de texto
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # Campos numéricos
    edad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.FloatField()

    # Campos de fechas
    fecha_nacimiento = models.DateField()
    ultimo_login = models.DateTimeField(auto_now=True)

    # Campos booleanos
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')