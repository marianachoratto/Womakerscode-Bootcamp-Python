"""
URL configuration for projeto_womakers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import inicio, cadastro

urlpatterns = [
    path('admin/', admin.site.urls), #area administrativa
    path('', inicio),
    path('cadastro/', cadastro),
    path('curso/', include('cursos.urls', namespace= 'cursos')),
    #a função include é como uma seta que joga para o resto da URL, que fica dentro dos aplicativos
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls', namespace='api'))
]


#A função include() no Django serve para duas finalidades principais, dependendo do contexto em que é utilizada: incluir URLs de uma aplicação em outra e incluir templates HTML dentro de outros templates.

'''O namespace no Django é usado para garantir que as URLs sejam únicas e possam ser referenciadas de forma segura, mesmo quando diferentes aplicações usam os mesmos nomes de URLs. Isso é especialmente útil em projetos que incluem múltiplas aplicações, onde pode haver conflitos de nomes entre as URLs. Ao definir um namespace para as URLs de uma aplicação, você cria um espaço de nomes único para essas URLs, permitindo que elas sejam referenciadas usando um identificador único, evitando assim conflitos.

Quando você usa a função include() para incluir as URLs de uma aplicação no seu projeto Django, você pode especificar um namespace para essas URLs. Isso adiciona um prefixo ao nome de cada URL incluída, facilitando a referência a essas URLs de forma única em todo o projeto. Por exemplo, se você tem uma aplicação chamada cursos e define namespace='cursos', você pode referenciar as URLs dessa aplicação como cursos:nome_da_url .

Além disso, o namespace pode ser usado para incluir a mesma aplicação mais de uma vez com um namespace diferente para cada instância. Isso é útil em situações onde você deseja reutilizar uma aplicação em diferentes partes do seu projeto, mas precisa evitar conflitos de nomes de URLs. Ao fornecer um namespace único para cada instância, você garante que as URLs de cada instância sejam únicas e possam ser referenciadas corretamente 1.'''