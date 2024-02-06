import sqlite3

conexao = sqlite3.connect('exercicios_sql')
cursor = conexao.cursor()

# cursor.execute(
#     'CREATE TABLE alunos(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(30), idade INT, curso VARCHAR(30))')

# dados = cursor.execute(
#     'INSERT INTO alunos(nome, idade, curso) VALUES("Mariana", 26, "analise e desenvolvimento de sistemas" )')
# dados = cursor.execute(
#     'INSERT INTO alunos(nome, idade, curso) VALUES("Luan", 27, "analise e desenvolvimento de sistemas" )')
# dados = cursor.execute(
#     'INSERT INTO alunos(nome, idade, curso) VALUES("Rafaela", 29, "farmacia" )')
# dados = cursor.execute(
#     'INSERT INTO alunos(nome, idade, curso) VALUES("Jake", 28, "Medicina" )')
# dados = cursor.execute(
#     'INSERT INTO alunos(nome, idade, curso) VALUES("Victoria", 28, "25" )')

# dados = cursor.execute(
#     'UPDATE alunos SET curso="analise e desenvolvimento de sistemas" WHERE nome="Luan"')

# dados = cursor.execute("UPDATE alunos SET curso='medicina' WHERE nome='Jake'")
# dados = cursor.execute("UPDATE alunos SET curso='medicina' WHERE nome='Victoria'")
# dados = cursor.execute("UPDATE alunos SET curso='medicina2' WHERE nome='Victoria'")

#----------------------------------------------------------
# cursor.execute("SELECT * FROM alunos")
# for item in dados: 
#     print(item)

#-----------------------------------------------------------
# cursor.execute("SELECT COUNT(*) FROM alunos")
# total = cursor.fetchone()[0]
# print(total)
#a função fetchone() também é propria do SQL e pega a próxima linha da tabela
#a função count() é propria do SQL

# cursor.execute(
#     "UPDATE alunos SET idade=18 WHERE nome='Victoria'"
# )
# -----------------------------------NOVA TABELA ----------------------------------------

# cursor.execute("CREATE TABLE clientes(id int PRIMARY KEY, nome varchar(30), idade int, saldo float )")

# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, 'joao victor', 26, 260.65)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, 'renata', 58, 5680)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, 'lucio', 61, 15460.98)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, 'sergio', 45, 765.37)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, 'laura', 18, 500.65)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, 'salvatore', 84, 452.48)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(7, 'dalila', 35, 800)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(8, 'samael', 35, 260.65)")

#CALCULANDO A MÉDIA DOS SALDOS
# cursor.execute('SELECT SUM(saldo) FROM clientes ')
# saldo = cursor.fetchone()[0]

# cursor.execute('SELECT COUNT(*) FROM clientes')
# numero_clientes = cursor.fetchone()[0]

# saldo_medio = saldo/numero_clientes
# print(saldo_medio)

#QUANTOS CLIENTES COM SALDO ACIMA DE MIL REAIS? 
# cursor.execute(
#     "SELECT COUNT(*) FROM clientes WHERE saldo>=1000"
# )
# saldo_superavitario = cursor.fetchone()[0]
# print(saldo_superavitario)

# cursor.execute("UPDATE clientes SET id=11 WHERE nome='joao victor'")
# cursor.execute("UPDATE clientes SET id=12 WHERE nome='renata'")
# cursor.execute("UPDATE clientes SET id=13 WHERE nome='lucio'")
# cursor.execute("UPDATE clientes SET id=14 WHERE nome='sergio'")
# cursor.execute("UPDATE clientes SET id=15 WHERE nome='laura'")
# cursor.execute("UPDATE clientes SET id=16 WHERE nome='salvatore'")
# cursor.execute("UPDATE clientes SET id=17 WHERE nome='dalila'")
# cursor.execute("UPDATE clientes SET id=18 WHERE nome='samael'")

# cursor.execute("CREATE TABLE compras(id int(2) PRIMARY KEY, cliente_id int(2), produto varchar(50), valor float)")

# cursor.execute("DROP TABLE compras")

# cursor.execute("CREATE TABLE compras ( id INT PRIMARY KEY, cliente_id int(2), produto varchar(50), valor float, FOREIGN KEY (cliente_id) REFERENCES clientes(id) );")

# cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES (99, 12, 'amaciante', 12.35)")
# cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES (98, 18, 'leite', 8)")
# cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES (97, 13, 'feijao', 4.15)")
# cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES (96, 12, 'arroz', 3.55)")

dados = cursor.execute("SELECT cliente_id FROM compras WHERE cliente_id=12")


conexao.commit()
conexao.close()

#O QUE APRENDEMOS? 
# não se esqueça de cortar a conexão, se não sua tabela não funciona 
# quando você define um campo como auto_increment, você precisa de uma primary_key. Os dois vem juntos. 
# quando o id vem automático, você não precisa escrever ele no código
# quando você mexer diretamente na tabela, não se esqueça de atualizar - senão, ela não se mexe
#se você mudar alguma coisa diretamente na tabela, você pode estar mudando para todo mundo
#o fetchone() retorna 1 valor de cada vez, o fetchall() retorna dois- uma tupla (linha, valor)
#No SQLITE você já tem que criar a tabela com uma foreign key
#Criar coluna de foreign key normalmente e colocar o comando de adicionar chave NO FINAL