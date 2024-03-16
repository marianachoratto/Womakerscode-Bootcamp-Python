'''Vamos verificar se a view está retornando o template esperado'''

import pytest
from pytest_django.asserts import assertTemplateUsed
#quando você quer verificar um template tem que utilizar esse método assertTemplateUsed

@pytest.mark.django_db
def test_curso_view_deve_retornar_template(client):
    response = client.get('/curso/criar_curso/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_curso.html')

#client chama o servidor. Próprio do pytest