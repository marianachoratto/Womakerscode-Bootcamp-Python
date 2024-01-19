#TRATAMENTO DE EXCEÇÕES

#Try e except: um if else especifico para tratamento de erros

def divisao(a, b):
    try:
        resultado = a/b
        print(resultado)
    except (ZeroDivisionError, TypeError):
        print('Erro: Impossivel existir um valor por zero')
    except TypeError as error: 
        print(f'Erro: Tentando dividir por uma string. Detalhes {error}')
    #posso colocar quantos excepts forem necessários
    
    
    

# divisao(2, 0)

#mais detalhado "as e"
# o {e} significa detalhes

# def divisao(a, b):
#     try:
#         resultado = a/b
#         print(resultado)
#     except TypeError as e: 
#         print(f'Erro: Tentando dividir por uma string. Detalhes {e}')

divisao(2, 'womarkerscode')