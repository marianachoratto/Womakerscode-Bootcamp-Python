# Construtor padrão
'''class MinhaClasse1: 
    def __init__(self):
        print('MinhaClasse1 chamou o construtor padrão')

objeto1 = MinhaClasse1()

#construtor implícito
class MinhaClasse2: 
        pass # não faz nada. Ele deixa a função passar sem dar erro 
        #NOTE! Foi criado um __innit__ implícito aqui que não é visto

objeto2 = MinhaClasse2()

# Construtor parametrizado
class MinhaClasse3:
    def __init__(self, param):
        print(f'MinhaClasse3: Chamou o construtor parametrizado com o parâmetro {param}')

objeto3 = MinhaClasse3('meu objeto')
Ao declarar um construtor parametrizado, o interpretador python não cria mais outro construtor

Destrutores 
class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome
        print(f'MinhaClasse1: Chamou o construtor padrão de {nome}')

    def __del__(self):
        print(f'MinhaClasse1: Chamou o destrutor de {self.nome}')

# O momento de execução de um destrutor é depois que o programa tem seu encerramento solicitado
print('Começou a execução do programa')
objeto1 = MinhaClasse('objeto1')
print('Vai terminar a execução do programa')'''
# exit() #Essa função é implícita, o python faria mesmo se vc não chamasse 

class Pessoa:   
    def falar_oi(self):  
        self.nome = 'Thais'        
        print(f'Oi, meu nome é {self.nome}')
 
pessoa = Pessoa() #Note! Aqui eu estou apenas definindo uma variável para a classe. Não chama nada. A variável pessoa recebe a classe pessoa 
pessoa.falar_oi() #Quem chama é essa função
