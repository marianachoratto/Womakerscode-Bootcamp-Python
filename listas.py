'''frutas= ['maçã', 'banana', 'laranja', 'uva']

frutas.append('carambola')
frutas.append(input('Digite uma fruta:'))

for item in frutas:
    print(item)

tupla = ('maça', 'uva')

# tupla.append('melancia')
print(tupla)

#DICIONÁRIO 

dicionario = {'Chave': 'valor'}
dicionario['maçã'] = 'é uma fruta'
dicionario['gato'] = 'é um animal'

print(dicionario)

computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250bg'}
print(computador.values())

# chave = list(computador.keys())
# print(chave)'''

dicionario = {'a': 1, 'b': 2, 'c': 3}
dicionario.pop('b')
print(dicionario) # Saída: {'a': 1, 'c': 3}