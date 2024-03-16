from django.shortcuts import render
#importanto rest framework 
from rest_framework.decorators import api_view
#importando o método response 
from rest_framework.response import Response
#importando serializer
from rest_framework.viewsets import ModelViewSet
from cursos.models import Curso
from rest_api.serializers import CursoModelSerializer

# Decorator para mostrar que é uma API. 
#Essa função pode ser acessada através dos métodos GET e POST 
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get('name')}'})
    return Response({'hello': 'World API'})

#Essa função ModelViewSet() habilita a visualização dos outros aplicativos para 3º
#Fizemos a conexão da API com o BD
class CursoModelViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    #pegando a função do arquivo serializers
    serializer_class = CursoModelSerializer


''' A queryset é essencialmente uma lista de instâncias de um modelo Django que você pode querer converter em um formato como JSON para enviar como resposta de uma API.
'''