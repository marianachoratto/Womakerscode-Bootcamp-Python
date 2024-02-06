class Produto:
    def __init__(self, nome, valor):
        self.nome = f' Carro {nome}'
        self.__valor = valor * 3
        pass

    def get_valor(self):
        return f'O valor do carro {self.nome} é {self.__valor + 300}' 
    
    def set_valor(self, novo_valor):
        if novo_valor < 30000:
            print('erro')
        else: 
            self.__valor = novo_valor + 7

carro = Produto('camaro amarelo', 5000)

print(carro.get_valor())

carro.set_valor(2)
#Você usa o set para mudar um valor. Esse valor pode ser QUALQUER VALOR (inclusive os protegidos e privados)

carro.set_valor(50001)
print(carro.get_valor())