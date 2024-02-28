from django.urls import path
from rest_api.views import hello_world

app_name = 'rest_api'
urlpatterns = [
    path('hello_word', hello_world, name= 'hello_word_API')
]

'''No Django, name e namespace são dois conceitos distintos usados principalmente no contexto de URLs e views.

name: O parâmetro name em uma URL é usado para identificar de forma única uma URL específica dentro do seu projeto Django. Isso permite que você referencie URLs em outras partes do seu código, como em templates ou em redirecionamentos, usando este nome único. Por exemplo, no seu código, name='hello_word_API' dá um nome único à URL hello_world, permitindo que você a referencie por este nome em outras partes do seu projeto.

namespace: O namespace é usado para evitar conflitos de nomes entre diferentes aplicações dentro de um projeto Django. Cada aplicação Django pode ter suas próprias URLs, e o namespace ajuda a diferenciar essas URLs. Quando você inclui as URLs de uma aplicação em seu projeto principal usando include(), você pode fornecer um namespace para essa inclusão. Isso adiciona um prefixo a todos os nomes de URLs definidos dentro dessa aplicação, permitindo que você use nomes de URLs duplicados em diferentes aplicações sem conflitos. Por exemplo, se você tiver duas aplicações, app1 e app2, e ambas tiverem uma URL chamada detail, você pode usar namespaces para diferenciá-las, como app1:detail e app2:detail.

Em resumo, o name é usado para dar um nome único a uma URL específica para facilitar a referência a ela em outras partes do projeto, enquanto o namespace é usado para evitar conflitos de nomes entre URLs de diferentes aplicações dentro de um projeto Django.'''