# a =  1
# print(type(a))

class Ave():
    def andar(self):
        print('andando')
    
    def voar(self):
        print('voando')

class Calopsita(Ave):
    def piar(self):
        print('piu piu')

class Pato(Ave):
    def quack(self):
        print('quack')

    def nadar(self):
        print('nadando')

# Como as variáveis não são tipadas, não é possível saber o tipo de uma variável em uma função
# A função não tem como garantir que o animal é de algum tipo específico, por exemplo, o tipo `Pato`
def executar_pato(animal):  #recebe o objeto animal
    animal.quack()
    animal.andar()
    animal.voar()
    animal.nadar()

pato = Pato()
calopsita = Calopsita()

executar_pato(pato)
executar_pato(calopsita)

#a unica forma de saber se o objeto que você está usando é do tipo que você quer é testando e olhando seus atributos 
#Se andar como um pato, fazer quack como um pato e voar como um pato, então é um pato.