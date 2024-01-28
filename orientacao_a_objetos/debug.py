#Estamos fazendo um código para um banco e estamos criando um aplicativo que vai monitorar o saldo da conta de um cliente. 
#o cliente recebe o salário bruto na conta e o banco retém uma parte para o IR 
# o sistema não deixa o cliente tirar mais do que o valor que tem na conta 

import colorama
colorama.init()

salario_bruto = 5000
valor_na_conta = -1
salario_processado = False

def imprimir_no_log(texto, nivel='info'):
    if nivel.lower() == 'info':
        print(colorama.Fore.LIGHTBLUE_EX + f'Info: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    elif nivel.lower() == 'aviso':
        print(colorama.Fore.YELLOW + f'Aviso: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    elif nivel.lower() == 'erro':
        raise ValueError(colorama.Fore.RED + 'Erro: ' + colorama.Style.RESET_ALL + texto)

def calcular_imposto_de_renda(valor):
    taxa = 0.27
    valor_imposto = taxa * valor
    return valor_imposto

def calcular_inss(valor):
    taxa = 0.14
    valor_imposto = taxa * valor
    return valor_imposto

def processar_salario():
    global valor_na_conta
    valor_irpf = calcular_imposto_de_renda(salario_bruto)
    valor_inss = calcular_inss(salario_bruto)
    valor_na_conta = salario_bruto - valor_irpf - valor_inss
    print(valor_na_conta)

def sacar_na_conta(valor):
    global valor_na_conta
    global salario_processado
    
    if not salario_processado:
        imprimir_no_log(f'Processando o salario bruto antes de permitir o saque...', 'aviso')
        processar_salario()
        imprimir_no_log(f'O novo valor do salário na conta é {valor_na_conta}...', 'info')
        salario_processado = True

    if valor <= valor_na_conta:
        valor_na_conta -= valor
        imprimir_no_log(f'Sacando {valor}. O novo saldo na conta é de {valor_na_conta}.', 'info')
    else:
        imprimir_no_log(f'A conta não possui saldo para sacar o valor de {valor}.', 'erro')
        return False

    return True