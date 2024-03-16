'''Sistema para a adoção de gatinhos
Vamos modelar um gatinho e uma pessoa 
'''

class Animal:
    #a função __init__ é o construtor. São as características default do animal.
    #Sempre que você for criar um animal, ele vai ter que ter esses atributos
    def __init__(self, nome, idade, cor):
        self.__nome = nome
        self.__idade = idade
        self.__cor = cor
        # self.__adotado = False
    
    #Mostrando individualmente essas características
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_cor(self):
        return self.__cor

#Por que utilizamos o self? 
#O self em Python é usado para representar a instância atual da classe e é um parâmetro comum em métodos de instância.  Quando você define um método dentro de uma classe, o primeiro parâmetro é self, que se refere à instância da classe. Isso permite que você acesse e modifique os atributos e métodos da instância atual da classe 124.

class Gato(Animal):
    def __init__(self, nome, idade, cor, raca):
        super().__init__(nome, idade, cor)
        self.__raca = raca
    
    def get_raca(self):
        return self.__raca

#Herança multiplas (não é suportada pelo python)
    #É herdar de 2 classes diferentes 
    #Por não ser suportada pelo python nós fazemos uma gambiarra, que é adotar animal e adotante como atributos
    #não pode usar a função super()

class Adotante: 
    def __init__(self, nome):
        self.nome = nome 

class AdocaoGatinho: 
    def __init__(self, animal, adotante):
        self.animal = animal
        self.adotante = adotante
    
animal01 = Animal('bento', 2, 'branco')
adotante01 = Adotante('Isadora')

#criar uma instancia de adoção,
adocao01= AdocaoGatinho(animal01, adotante01)

#É igual a isso 
adocao01= AdocaoGatinho(Animal('bento', 2, 'branco'), Adotante('Isadora') )

print('Nome do gatinho:', adocao01.animal.get_nome())
print('Idade do gatinho:', adocao01.animal.get_idade())
print('Nome do adotante:', adocao01.adotante.nome)


#Vamos criar um objeto
# gatinho1 = Animal('Bolinha', 2, 'branco')
# gatinho2 = Animal('Python', 30, 'verde')
# gatinho3 = Gato('Frajola', 5, 'preto', 'vira-lata')

# print(gatinho2.get_nome())
# print(gatinho3.get_raca())

