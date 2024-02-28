from django.shortcuts import render
#importanto rest framework 
from rest_framework.decorators import api_view
#importando o método response 
from rest_framework.response import Response

# Decorator para mostrar que é uma API. 
#Essa função pode ser acessada através dos métodos GET e POST 
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get('name')}'})
    return Response({'hello': 'World API'})