import re
from django.shortcuts import render
from .serializers import * 
from rest_framework import viewsets
from .models import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

class register(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class RegistrarUsuario(APIView):
    def post(self, request):
        if request.method == "POST":
            name = request.data["name"]
            last = request.data["last"]
            email = request.data["email"]
            password1 = request.data["password"]
            password2 = request.data["confirmPassword"]

            if name == "" or email == "" or last == "" or password1 == "" or password2 == "":
                return Response(data={'message': 'Todos los campos son obligatorios', 'respuesta': 400}, status=400)
            elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return Response(data={'message': 'El correo no es válido', 'respuesta': 400}, status=400)
            elif password1 != password2:
                return Response(data={'message': 'Las contraseñas no coinciden', 'respuesta': 400}, status=400)
            else:
                try:
                    q = Users(
                        name=name,
                        last = last,
                        email=email,
                        password=password1,

                    )
                    q.save()
                except Exception as e:
                    return Response(data={'message': 'El Usuario ya existe', 'respuesta': 409}, status=409)

        #
        return Response(data={'message': f'Usuario creado correctamente. Tu nombre es: {name}', 'respuesta': 201}, status=201)


# esto es para logirse un usuario
class LoginUsuario(APIView):
    def post(self, request):
        if request.method == "POST":
            email = request.data["email"]
            password = request.data["password"]

            if  email == ""  or password == "":
                return Response(data={'message': 'Todos los campos son obligatorios', 'respuesta': 400}, status=400)
            elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return Response(data={'message': 'El correo no es válido', 'respuesta': 400}, status=400)
            else:
                try:
                    q = Users.objects.get(email = email)
                    if(q.password == password):
                        return Response(data={'message': f'Logueando !!. Tu email es: {q.email}', 'respuesta': 200}, status=200)
                    else:
                        return Response(data={'message': f'No es la contraseña correcta !!', 'respuesta': 400}, status=400)
                except Exception as e:
                    return Response(data={'message': 'El Usuario no existe', 'respuesta': 409}, status=409)

        

class DeleteUser(APIView):
    def delete(self,request,id):
        #esto es para eliminar un usuario
        try:
            u = Users.objects.get(pk=id)
            u.delete()
            return Response(data={
                'message':'Usuario no existe !!',
                'respuesta': 200
            })
        except Exception as e:
            return Response(data={
                'message':'Usuario no existe !!',
                'respuesta': 404
            })


class CreateLey(APIView):
    def post(self,request):
        # esto es para crear una ley
        pass

        
        
