## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    tamanho = 0
    soma = 0.0
    for i in valores:
        soma += i
        tamanho += 1
    print(tamanho, soma)
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    try:
        if valor.lower() == 'ok':
            continuar = False
        else:
            valor = float(valor)
            valores.append(valor)
    except ValueError as e:
        print(f'Sintaxe inválida.  {e}. Tente novamente')
    

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))

# Como comparar valores em python?
# if type(valor) is int: