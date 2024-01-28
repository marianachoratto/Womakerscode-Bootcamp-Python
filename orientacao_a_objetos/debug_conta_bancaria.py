import debug
import colorama

colorama.init()

print('Seu salário bruto é de {}'.format(debug.salario_bruto))
valor_a_sacar = input('Quanto você deseja retirar da sua conta? ')
funcionou = debug.sacar_na_conta(float(valor_a_sacar))

# Sacando novamente
valor_a_sacar = input('Quanto você deseja retirar da sua conta? ')
funcionou = debug.sacar_na_conta(float(valor_a_sacar))