'''
GERENCIAMENTO DE MERCADO

Vamos criar um sistema orientado a objetos para representar um
sistema de mercado seguindo os requisitos fornecidos:

1. Cada produto pode ter um ou mais fornecedores.

2. O mercado controla apenas o nome, o telefone e o endereço de
cada cliente.

3. Cada produto tem um nome, uma lista de categorias às quais
pertence e uma quantidade disponível em estoque.

4. Quando um produto é comprado, sua quantidade disponível em
estoque é reduzida.

5. O mercado mantém um registro de todas as transações
realizadas, incluindo detalhes como data da compra, cliente
envolvido e quantidade de produtos comprados.

Responsáveis: 

'''
import sqlite3 

conexao = sqlite3.connect('mercado')
cursor = conexao.cursor()


# Criando a classe Cliente
class Cliente:
    #Construtor da classe cliente
    def __init__(self,id_cliente, nome_cliente, telefone_cliente, endereco_cliente):
        self.nome_cliente = nome_cliente
        self.id_cliente = id_cliente
        self.telefone_cliente = telefone_cliente
        self.endereco_cliente = endereco_cliente

    # Criando Getters e Setters 
        
    # Nome -------------------------------------------
    def nome_clienteGet(self):
        return self.nome_cliente

    def nome_clienteSet(self, nome_cliente):
        self.nome_cliente = nome_cliente

    # ID ----------------------------------------------
    def id_clienteGet(self):
        return self.id_cliente

    def id_clienteSet(self, id_cliente):
        self.id_cliente = id_cliente

    # Telefone ----------------------------------------
    def telefone_clienteGet(self):
        return self.telefone_cliente

    def telefone_clienteSet(self, telefone_cliente):
        self.telefone_cliente = telefone_cliente

    # Endereço ----------------------------------------
    def endereco_clienteGet(self):
        return self.endereco_cliente

    def endereco_clienteSet(self, endereco_cliente):
        self.endereco_cliente = endereco_cliente    

    # Criando a função STR
    def __str__(self):
        return f'Cliente {self.nome_clienteGet()}, de ID {self.id_clienteGet()}, telefone {self.telefone_clienteGet()} e endereço {self.endereco_clienteGet()}'

    # Criando função para retornar a lista clientes 
    def __repr__(self):
        return f'Cliente {self.nome_clienteGet()}, de ID {self.id_clienteGet()}, telefone {self.telefone_clienteGet()} e endereço {self.endereco_clienteGet()}'

#-----------------------------------------
# Criando a classe Produto
class Produto:
    # Fazendo Construtor
    def __init__(self, id_produto, nome_produto, categorias, qnt_disponivel, id_fornecedor):
        self.id_produto = id_produto,
        self.nome_produto = nome_produto,
        self.categorias = categorias 
        self.qnt_disponivel = qnt_disponivel
        dados = cursor.execute(f"SELECT * FROM fornecedores WHERE id={id_fornecedor}")
        fornecedor_fetch = dados.fetchone()
        self.fornecedor = Fornecedor(fornecedor_fetch[0], fornecedor_fetch[1], fornecedor_fetch[2], fornecedor_fetch[3])

    def __str__(self):
        return f'O produto de ID {self.id_produto} é {self.nome_produto}, está na categoria {self.categorias}. Seu estoque atualmente é de {self.qnt_disponivel}'

    def __repr__(self):
        return f'O produto de ID {self.id_produto} é {self.nome_produto}, está na categoria {self.categorias}. Seu estoque atualmente é de {self.qnt_disponivel}'

    # Fazendo função de diminuir o estoque
    def diminuirEstoque(self, qtd):
        if (qtd > self.qnt_disponivel):
            print(f"Não há essa quantidade do produto disponível. O estoque atual é de {self.qnt_disponivel}. Tente novamente")
        else:
            self.qnt_disponivel -= qtd
            cursor.execute(f'UPDATE produtos SET quantidade={self.qnt_disponivel} WHERE id={self.id_produto[0]}')
            print("Produto comprado com sucesso!")
        

    # Criando Getters e Setters do Produto
        
    # Nome -------------------------------------------
    def nome_produtoGet(self):
        return self.nome_produto

    def nome_produtoSet(self, nome_produto):
        self.nome_produto = nome_produto

    # Categorias ----------------------------------------------
    def categoriasGet(self):
        return self.categorias

    def categoriasSet(self, categorias):
        self.categorias = categorias

    # Quantidade Disponível ----------------------------------------
    def qnt_disponivelGet(self):
        return self.qnt_disponivel

        #O que essa função faz? 
    def qnt_disponivelGet(self, qnt_disponivel):
        self.qnt_disponivel = qnt_disponivel

# ---------------------------------------------------------------------


# Criando a classe Fornecedor
class Fornecedor:
    # Fazendo o Contrutor
    def __init__(self, id_fornecedor, nome_fornecedor, endereco_fornecedor, telefone_fornecedor):
        self.nome_fornecedor = nome_fornecedor
        self.endereco_fornecedor = endereco_fornecedor
        self.telefone_fornecedor = telefone_fornecedor
        self.id_fornecedor = id_fornecedor


    # Criando Getters e Setters do Fornecedor

    # Nome --------------------------------------------
    def nome_fornecedorGet(self):
        return self.nome_fornecedor

    def nome_fornecedorSet(self, nome_fornecedor):
        self.nome_fornecedor = nome_fornecedor

    # Endereço ----------------------------------------
    def endereco_fornecedorGet(self):
        return self.endereco_fornecedor

    def endereco_fornecedorSet(self, endereco_fornecedor):
        self.endereco_fornecedor = endereco_fornecedor

    # Telefone ----------------------------------------
    def telefone_fornecedorGet(self):
        return self.telefone_fornecedor

    def telefone_fornecedorGet(self, telefone_fornecedor):
        self.telefone_fornecedor = telefone_fornecedor

# ---------------------------------------------------------------------
# CLASSE MERCADO 

class Mercado:
    # print('Bem vindo ao mercado!')
    # doesClienteExiste = input('Você já é cliente? Digite S ou N:  ').upper()
    # if doesClienteExiste == 'S':
    #     nome_cliente = input('Digite seu nome:').lower()
    #     dados = cursor.execute(f'SELECT * FROM clientes WHERE nome="{nome_cliente}" ')
    #     cliente_fetch = dados.fetchone() ## retorna uma tupla
    #     # print(cliente_fetch) 
    #     # print(cliente_fetch[2])
    #     cliente_atual = Cliente(cliente_fetch[0], cliente_fetch[1], cliente_fetch[2], cliente_fetch[3])
    #     print(cliente_atual)

    #     conexao.commit()
    #     conexao.close()
        
    # if doesClienteExiste == 'N':
    #     # id_cliente = int(input('Digite o ID do cliente: '))
    #     nome_cliente = input('Digite o nome do cliente:   ')
    #     telefone_cliente = int(input('Digite o telefone do cliente:   '))
    #     endereco_cliente = input('Digite o endereço do cliente:   ')
    #     cursor.execute(f'INSERT INTO clientes(nome, endereco, telefone) VALUES("{nome_cliente}", "{telefone_cliente}", "{endereco_cliente}");')
    #     print("Parabéns, você foi cadastrado!")

    escolha_produto = int(input(f'Qual produto você quer comprar? Digite o número: \n 1-arroz, \n 2-feijão, \n 3-alface \n 4-cenoura \n 5-banana \n 6-laranja \n 7-amaciante \n 8-sabão em pó \n' ))
    dados = cursor.execute(f'SELECT * FROM produtos WHERE id={escolha_produto}')
    produtos_fetch = dados.fetchone()
    print("PRINT: ", produtos_fetch[0])
    produto_comprado = Produto(produtos_fetch[0], produtos_fetch[1], produtos_fetch[2], produtos_fetch[3], produtos_fetch[4])
    print(produto_comprado)

    diminuir_estoque = int(input("Você quer comprar quantas unidades deste produto?  "))
    produto_comprado.diminuirEstoque(diminuir_estoque)

    conexao.commit()
    conexao.close()

# Criar tabela de registro ---> - Calcular o total de vendas por categoria de produto.
# Colocar a possibilidade de vários fornecedores 
#

