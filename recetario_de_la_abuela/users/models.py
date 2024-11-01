from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(default=0)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
   

    # Comentar en caso de necesidad para crear más superusuarios
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username