from abc import ABC, abstractmethod

'''Ex: Você trabalha na Nintendo e está criando um jogo que tem novos pokemons. Para criar o seu pokemon CharizardBlue você vai usar como base a API já existente da Nintendo para manter o padrão dos pokemons '''
'''Todo o pokemon tem um ataque principal, um método de evolução e uma propriedade para definir o seu nome e outra o seu tipo.'''


# A classe base dos pokemons. Todo o pokemon que criarmos vai ter que herdar dela.
class BasePokemon(ABC):
    def __init__(self, nome):
        self.nome = nome
        self._nivel = 1             #nivel e experiencia são atributos protegidos 
        self._experiencia = 0

    @abstractmethod
    def ataque_principal(self): # O uso de métodos abstratos torna a classe abstrata
        pass

    @abstractmethod
    def passar_de_nivel(self):
        pass

    @abstractmethod
    def evoluir(self):
        pass

    @property
    @abstractmethod
    def tipo(self):
        pass

# Criar um objeto de uma classe abstrata gera um erro
# pokemon = BasePokemon('Pikachu', 'Elétrico')
#Output: TypeError: Can't instantiate abstract class BasePokemon without an implementation for abstract methods 'ataque_principal', 'evoluir', 'passar_de_nivel', 'tipo'

class Pikachu(BasePokemon):
    def __init__(self, nome):
        super().__init__(nome)

    def ataque_principal(self):
        print(f'{self.nome} usou Choque de trovão!')
        self._experiencia += 2
        self.passar_de_nivel()

    def passar_de_nivel(self):
        # Passa de nível a cada 10 pontos de experiência
        if self._experiencia % 10 == 0:
            self._nivel += 1
            print(f'{self.nome} passou para o nível {self._nivel}!')
            self.evoluir()

    def evoluir(self):
        if self._nivel == 25:
            print('!!!! Evoluiu para Raichu !!!!')
            self.nome = 'Raichu'

    @property
    def tipo(self):
        return 'Elétrico'
    #NOTE! Essa propriedade só tem o método getter e não o setter, então não posso alterá-la. 
    
    def ataque_secundario(self):
        print(f'{self.nome} usou Surra de Calda!')
        self._experiencia += 2
        self.passar_de_nivel()
    #Note! Eu usei todos os métodos e propriedades da API, mas isso não me limita, pois eu posso criar métodos novos

pokemon = Pikachu('Pikachu')
print(pokemon.nome + ' é um pokemon do tipo ' + pokemon.tipo)

for _ in range(125):
    pokemon.ataque_principal()
    pokemon.ataque_secundario()