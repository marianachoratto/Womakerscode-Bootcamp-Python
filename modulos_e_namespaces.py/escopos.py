bebida = 'refrigerante'

def cardapio():
    comida = 'hamburguer'
    bebida = 'suco'  #foi criada uma variável local com o mesmo nome da variável global
    print('comida', comida)
    print('bebida', bebida)

cardapio()
print('bebida', bebida)