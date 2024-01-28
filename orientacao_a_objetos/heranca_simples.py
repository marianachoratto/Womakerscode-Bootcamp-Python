class Pessoa: 
    def __init__(self, nome):
        self._nome = nome
        self._tipo = 'Pessoa'
    
    def falar_oi(self):
        print('Oi! Meu nome é {}'.format(self._nome))
    
    def falar_tipo(self):
        print('Meu tipo é {}'.format(self._tipo))

pessoa1 = Pessoa('Naiara')
pessoa1.falar_oi()
pessoa1.falar_tipo()

# A classe estudante é derivada da classe Pessoa.
# Relação é: "Estudante" é uma "Pessoa"

class Estudante(Pessoa): #dentro dos () colocar a classe pai
    def __init__(self, nome, curso):
        super().__init__(nome) # chama o construtor da classe base
        self._curso = curso
    
    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso "{self._curso}"') # A propriedade self._nome é herdada da classe base

    #Como sobrescrever uma classe original? Só escrever um nome método 
    def falar_tipo(self):
        self.tipo = 'estudante'
        return super().falar_tipo() #chamando o print da função falar_tipo() original

pessoa2 = Estudante('Yasmin', 'Introdução ao Python')
pessoa2.falar_curso()
pessoa2.falar_tipo

#Como testar se um objeto é instância de uma determinada classe? 
print('O objeto estudante é uma instância da classe Estudante? ', isinstance(pessoa2, Estudante))
print('O objeto estudante é uma instância da classe Pessoa? ', isinstance(pessoa2, Pessoa))
print('A classe Estudante é uma sub-classe de Pessoa? ', issubclass(Estudante, Pessoa))
print('A classe Pessoa é uma sub-classe de Estudante? ', issubclass(Pessoa, Estudante))
print()

# Em Python, todos as classes herdam implicitamente da classe object
class Humano:
    pass

# A classe Humano já começa com vários atributos e métodos
humano = Humano()
print(dir(humano))
print()

# Esses mesmos atributos e métodos existem nas classes que declaramos acima
# print(dir(professora))
# print()