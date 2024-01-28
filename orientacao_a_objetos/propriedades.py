class Quadrado:
    def __init__(self, medida):
        self.altura = medida
        self.largura = medida
    #Não são mais atributos, são propriedades, pois nós demos o selo de propriedade abaixo

    @property
    def altura(self):
        print('getter de altura') #consolelog de confirmação
        return self.__medida

    @altura.setter
    def altura(self, valor):
        print('setter de altura')
        if valor < 0:
            raise ValueError()
        self.__medida = valor

    @property
    def largura(self):
        print('getter de largura')
        return self.__medida

    @largura.setter
    def largura(self, valor):
        print('setter de largura')
        if valor < 0:
            raise ValueError()
        self.__medida = valor

    def area(self):
        return self.largura * self.altura

quadrado = Quadrado(2)
quadrado.altura = 3
print(quadrado.area())

'''
Quando criamos o objeto quadrado, vemos que os setters são chamados.
Quando acessamos os valores, vemos que os getters são chamados.
Se removemos um dos setters, não conseguimos mais alterar o valor da propriedade diretamente.
'''