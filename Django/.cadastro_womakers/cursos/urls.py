#página opcional
from django.urls import path 
from cursos.views import criar_curso

app_name = 'Cursos'
urlpatterns = [
    #todas as sub-urls vão ficar nesse módulo deixando codigo mais organizado. Ex: criar, delete, alterar 
    path('criar_curso/', criar_curso, name='criar_curso')
]

#ISSO NÃO EXCLUI NOSSO DEVER DE INFORMAR NAS URLS DE CONFIGURAÇÕES GERAIS 
#para chegar até a url fica "curso/criar_cursos"