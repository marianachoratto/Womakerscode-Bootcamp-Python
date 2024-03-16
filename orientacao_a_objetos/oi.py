# class Dobrador:
#     tipo_da_dobra = "Terra"

#     def atacar(self):
#         print("O dobrador atacou!")

# dobrador_1 = Dobrador()

# dobrador_1.atacar()

class Dobrador:
    tipo_da_dobra = "Terra"

    nome_do_dobrador = "Katara"

    def atacar(self):
        print("O dobrador atacou!")

    # def mudar_dobra(self):
    #     tipo_da_dobra = "Água"
        #esse atributo tipo_da_dobra tem escopo local apenas. Ele só existe dentro dessa função
    
    def mudar_dobra(self):
        self.tipo_da_dobra = "Água"

dobrador_3 = Dobrador()

dobrador_3.mudar_dobra()
print(dobrador_3.tipo_da_dobra) #você não chama a função de novo. Você chama o atributo (que já mudou)
