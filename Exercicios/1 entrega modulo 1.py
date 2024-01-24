# MODULO 1 - CONCEITOS BÁSICOS

#EXERCICIO 2
'''
Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
'''

# ano_nascimento = int(input('Digite o ano do seu nascimento:'))
# print(f'Você tem {2024 - ano_nascimento} anos')

#Responsável: Mariana Choratto 
#-----------------------------------------------------------------------
# EXERCICIO 3 
'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros

numero = int(input('Digite um numero em km:'))

conversao_metros= numero * 1000

print(
    conversao_metros
)'''

#------------------------------------
#EXERCICIO 4
''' Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''


#------------------------------------
#EXERCICIO 5
'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''
'''
sal_bruto = float(input('Qual o salário bruto?'))

if sal_bruto <= 1903.98:
    print(f'O salário liquído é {sal_bruto}.')
elif sal_bruto <=  2826.65:
    sal_liq = sal_bruto * 0.925
    print(f'O salário liquído é {sal_liq}')
elif sal_bruto <=  3751.05:
    sal_liq = sal_bruto * 0.85
    print(f'O salário liquído é {sal_liq}')    
elif sal_bruto <=  4664.68:
    sal_liq = sal_bruto * 0.775
    print(f'O salário liquído é {sal_liq}')   
else:
    sal_liq = sal_bruto * 0.725
    print(f'O salário liquído é {sal_liq}') 

#--------------------------------------------------------------------------------
#EXERCICIO 6 
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
 avião = 600 km/h
 carro = 100 km/h
 ônibus = 80 km/h'''

'''def calcular_tempo(distancia, velocidade):
    tempo = distancia/velocidade
    return tempo

distancia = float(input('Diga a distância do seu percurso (em km):'))  #existe uma função de converter

velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

print(
    f'O tempo da viagem por avião é: {calcular_tempo(distancia, velocidade_aviao):.1f} horas.'/n
    f'O tempo da viagem por carro é: {calcular_tempo(distancia, velocidade_carro):.1f} horas./n'
    f'O tempo da viagem de ônibus é: {calcular_tempo(distancia, velocidade_onibus):.1f} horas./n
    )'''

#-------------------------------------------------------------
#EXERCÍCIO 8
'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

# salario_hora = float(input('Digite qual o valor do seu salário/hora'))
# tempo_trabalho = float(input('Digite quantas horas você trabalha no mês'))

# def salario(hora, trabalho):
#     salario_total= hora * trabalho
#     return salario_total

# print(salario(salario_hora, tempo_trabalho):.2f)

#----------------------------------------------------------------
#EXERCÍCIO 9 

'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''



#-------------------------------------------------------------------
#EXERCÍCIO 10
'''Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.

Lembrando que para o retorno vamos usar print com as variáveis
criadas e este texto é somente um exemplo, utilizem a criatividade.'''

#--------------------------------------------------------------------
#MODULO 2 

#Exercicio 1 
''' Faça um Programa que peça dois números e imprima o maior deles.
'''

# numero1 = float(input('Digite um numero: '))
# numero2 = float(input("Digite outro numero: "))

# if numero1 > numero2:
#     print(numero1)
# else:
#     print(numero2)

#------------------------------------------------------------------
#MODULO 2
#EXERCICIO 2 (entrega)
'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

# resposta = input('Em que turno você estuda? \n Digite M para Matutino. \n Digite V para vespertino. \n Ou N para noturno.').upper()


# if resposta == "M": 
#     print("Bom dia!")
# elif resposta == "V":
#     print('Boa Tarde!')
# else:
#     print('Boa noite!')


#-----------------------------------------------------------------
# MODULO 3

#Exercicio 3 (Entrega)
'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''

# lista_de_compras = {
#     'arroz': 26,
#     'feijao': 12,
#     "ovo": 6, 
#     "alface": 3, 
#     "tomate": 4.5
# }

# preco_das_compras = lista_de_compras.values()

# soma_dos_valores = sum(preco_das_compras)

# print(f'O valor das compras foi de: {"{:.2f}".format(soma_dos_valores)}')

#----------------------------------------------------------------
#MODULO 4

'''Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.'''

# numero1 = int(input("Vamos digitar 3 numeros. \n Digite o primeiro número: "))
# numero2 = int(input(" Digite o segundo número: "))
# numero3 = int(input("Digite o terceiro número: "))

# def soma(numero1, numero2, numero3):
#     calculo = numero1 + numero2 + numero3
#     return calculo

# resultado = soma(numero1, numero2, numero3)
# print(f'O resultado da soma é {resultado}.')

#---------------------------------------------------------
"""  Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas """

# lado_1 = int(input("Digite o primeiro lado do triângulo:"))
# lado_2 = int(input("Digite o segundo lado do triângulo:"))
# lado_3 = int(input("Digite o terceiro lado do triângulo:"))

# if lado_1 == lado_2 == lado_3:
#     print('Triângulo equilátero')
# elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
#     print('Triângulo isóceles')
# else: 
#     print('Triângulo escaleno')

#---------------------------------------------------
""" Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais. """


#------------------------------------------------------
'''
 Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
'''

# numero = input('Digite um numero com mais de 2 algarismos:')

# def numero_reverso(numero):
#     array_numero = list(numero)
#     nova_lista = []
#     for i in array_numero[::-1]:
#         nova_lista.append(i)
#         print(nova_lista)
                

# numero_reverso(numero)

#O que aprendemos? 
#Existe a função list(), que quebra a string em uma lista. 
#Você passa a variável dentro do (). Assim: list(variavel)
#Para imprimir uma lista de trás para frente você pode usar [::-1]. O -1 é a indexação negativa e os 2 pontos: servem para dizer como a função vai rodar. 
#A sintaxe dos pontos é [inicio:fim:pulos]
#The first : represents the start index of the slice. By leaving it empty, you're telling Python to start at the beginning of the sequence.
# The second : represents the stop index. Again, by leaving it empty, you're telling Python to go until the end of the sequence.
# The -1 after the final : is the step. A step of -1 means to go backwards through the sequence.

#------------------------------------------------------------
'''
Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função

Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
desejada, onde esse menu chama a função de conversão correta.

Responsável: Laura Perroni Quadros da Silva
'''

# pergunta = (input('Você quer a temperatura em celsius ou farenheit? Digite C para celsius e F para Farenheit')).upper()

# def conversao_farenheit(graus_celsius):
#     farenheit = (graus_celsius*1.8) + 32
#     print(farenheit)

# def conversao_celsius(graus_farenheit):
#     celsius = (graus_farenheit - 32)/1.8
#     print(celsius)

# if pergunta == 'C' :
#     graus_celsius = int(input('Digite a temperatura em graus:'))
#     conversao_farenheit(graus_celsius)
# elif pergunta == 'F': 
#     graus_farenheit = int(input('Digite a temperatura em farenheit:'))
#     conversao_celsius(graus_farenheit)

#----------------------------------------------------------------
#CONTADOR DE VOGAIS 
frase_usuario = input("Digite uma frase: ")

def contador_vogais(frase_usuario):
    contador = 0
    vogais = 'aeiouAEIOU'
    array = list(frase_usuario)
    for item in array: 
        if item in vogais: 
            contador += 1
    return contador 

resultado = contador_vogais(frase_usuario)
print(f'A frase "{frase_usuario}" tem {resultado} vogais.')