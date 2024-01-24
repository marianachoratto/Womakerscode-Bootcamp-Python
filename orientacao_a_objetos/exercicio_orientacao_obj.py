# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'amarelo'
        self.velocidade = 0
    
    def ligar_carro(self):
        self.ligado = True

    def desligar_carro(self):
        self.ligado = False
    
    def acelerar_carro(self):
        self.velocidade += 10
    
    def desacelerar_carro(self):
        self.velocidade -= 10
    
    def parar_carro(self):
        self.velocidade = 0 

# Crie uma instância da classe carro.
fiat0303 = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
fiat0303.acelerar_carro()
print(f'A velocidade do carro é de {fiat0303.velocidade} km/h')

#Se você quer acelerar o carro 5x você tem que fazer um looping 
for _ in range(5):
    fiat0303.acelerar_carro()
print(f'A velocidade do carro é de {fiat0303.velocidade} km/h')
    # A função range() serve para catalogar numeros num looping


# Faça o carro "parar" utilizando os métodos da sua classe.
fiat0303.parar_carro()
print(f'O carro parou. A velocidade chegou a {fiat0303.velocidade} km/h')