from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
                                    

class RegisterView(APIView):
    def post(self, request):
        #print("Registro de Usuario")
        #return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener los datos del usuario logueado
# Esta vista sirve para ver los datos de mi propio perfil, cuando estoy logueado y le doy en "mi perfil"
class UserView(APIView):
     permission_classes = [IsAuthenticated]

     def get(self, request):
         serializer = UserSerializer(request.user)
         return Response(serializer.data)
     
    # sobreescribir para modificar los datos del usuario logueado:
    # Esta vista nos va a servir para modificar algún dato de 'mi perfil', por ejemplo, mi dirección, teléfono etc.
     
     def put(self, request):
         user = User.objects.get(id=request.user.id)
         serializer = UserUpdateSerializer(user, request.data)

         if serializer.is_valid(raise_exception=True):
             serializer.save()
             return Response(serializer.data)
         
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

     

        
    