from rest_framework import serializers
from users.models import User


# Serializador para la creación de Usuarios

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # A él serializador se le debe informar cual es el modelo que va a usar
        fields = ['id','email','username','password']   # A él serializador se le debe informar cuales son los campos que va a formatear o a serializar, estos datos deben nombrarse como se llaman en el modelo.

# Override método crear usuarios con password encriptado:

    def create(self, validated_data):
        passwords = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if passwords is not None:
            instance.set_password(passwords)
        instance.save()
        return instance
    
# Nuevo serializador para una consulta (GET)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username', 'first_name', 'last_name']

#Serializador para actualizar los campos del usuario (PUT):
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']