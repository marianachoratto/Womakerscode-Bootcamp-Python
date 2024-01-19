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
salario_bruto = float(input('Digite seu salário bruto:'))

if salario_bruto <= 1903.98:
    print(f'Você é isento de IR. Seu salário líquido é igual a {salario_bruto}')
elif salario_bruto <= 2826.65:
    ir2 = salario_bruto - (salario_bruto * 0.075)
    print(f'Sua alíquota de IR é de 7,5%. Seu salário líquido é igual a {ir2}')
elif salario_bruto <= 3751.05:
    ir3 = salario_bruto - (salario_bruto * 0.15)
    print(f'Sua alíquota de IR é de 15%. Seu salário líquido é igual a {ir3}')
elif salario_bruto <= 4664.68:
    ir4 = salario_bruto - (salario_bruto * 0.225)
    print(f'Sua alíquota de IR é de 22,5%. Seu salário líquido é igual a {ir4}')
else salario_bruto > 4664.69:
    ir5 = salario_bruto - (salario_bruto * 0.275)
    print(f'Sua alíquota de IR é de 27,5%. Seu salário líquido é igual a {ir5}')'''

#--------------------------------------------------------------------------------
#EXERCICIO 6 
'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

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

resposta = input('Em que turno você estuda? \n Digite M para Matutino. \n Digite V para vespertino. \n Ou N para noturno.').upper()


if resposta == "M": 
    print("Bom dia!")
elif resposta == "V":
    print('Boa Tarde!')
else:
    print('Boa noite!')


#-----------------------------------------------------------------
# MODULO 3

#Exercicio 3 (Entrega)
'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''

