from django.urls import path
from rest_api.views import hello_world, CursoModelViewSet
from rest_framework.routers import SimpleRouter
#não é uma boa prática usar outra linha para importar algo de algum lugar que já tem importações anteriores. Utilizar vírgula 
# import rest_api.views import CursoModelViewSet

app_name = 'rest_api'
urlpatterns = [
    path('hello_word', hello_world, name= 'hello_word_API')
]

#passando o SimpleRouter para o arquivo
router = SimpleRouter(trailing_slash= False)
#trailing_slash= False não adiciona uma / no final da url 

#registrando o caminho para o end-point. 1º parâmetro) o prefixo da url. 2º) função associada 
#para ver essa página é "api/curso"
router.register('curso', CursoModelViewSet )

#concatenação simples. Isso está adicionando todas as urls que porventura vierem a ser criadas dentro do urlpatterns 
urlpatterns += router.urls

'''O SimpleRouter vai criar as funções de GET, POST, PUT... automaticamente'''

