# def test_config():
#     assert 1==1

'''A palavra-chave assert em Python é usada para testar uma condição e verificar se ela é verdadeira. Se a condição for verdadeira, o programa continua sua execução normalmente. Por outro lado, se a condição for falsa, o assert interrompe a execução do programa e levanta uma exceção AssertionError. Essa exceção pode ser acompanhada por uma mensagem opcional que descreve o problema. '''
'''--------------------------------------------------------------------------------'''
'''Vamos testar essa função:
# def __str__(self):
#         return f'{self.titulo}: {self.data_do_curso} - {self.carga_horaria}'

'''

import pytest
from model_bakery import baker
#Essa biblioteca cria uma api entre esse arquivo e o banco de dados 
from cursos.models import Curso
from datetime import date

#a biblioteca baker vai criar uma instância de curso que nós criamos no banco de dados e depois comparar

#É um decorator que serve como chamamento 
@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo = 'Java',
        data_do_curso = date.today(),
        carga_horaria= '40'
    )
    
    return curso

#Essa é a função "geral" que pode ser utilizada para várias partes do código
@pytest.mark.django_db
def test_str_deve_retornar_string(curso):
    assert str(curso) == 'Java: 2024-03-05 - 40'