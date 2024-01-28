class Pessoa: 
    def __init__(self, nome, profissao, identidade):
        self._nome = nome      #atributo protegido 
        self.profissao = profissao
        self.__identidade = identidade  #atributo privado. Ninguém mexe, tanto que ele fica transparente 

    def __str__(self):
        return f'Nome: {self._nome}, Profissão: {self.profissao}, Identidade: {self.__identidade}'

pessoa1 = Pessoa('Marta Lima', 'astronauta', '12345')
print(pessoa1)

#vamos tentar alterar a profissão (atributo público)
pessoa1.profissao = 'programadora'
print(pessoa1)
#altera sem problemas 

#Se tentarmos alterar um atributo protegido, vamos conseguir também 
pessoa1._nome = 'Marta Calto'
print(pessoa1)

#Porém, não conseguimos alterar o atributo privado 
pessoa1.__identidade = '2222'
print(pessoa1)
#NOTE! O python não dá nem mensagem de erro, simplesmente não altera