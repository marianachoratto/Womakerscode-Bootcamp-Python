import sqlite3

    #Fazendo a conexão do arquivo python com o banco de dados e passando para uma variável
conexao = sqlite3.connect('Banco')
cursor = conexao.cursor()

# cursor.execute(
#     'CREATE TABLE usuarios( id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#NOTE! Comandos do SQL ficam em maiusculos, assim como o tipo de variável

# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#--------------------------------------------
# cursor.execute(
#     'CREATE TABLE produtos( id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('DROP TABLE produtos')
#---------------------------------------------

# cursor.execute("INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(1, 'Isadora', 'Rua camaleão vermelho, 345, Salvador', 'isa@gmail.com', 123456)")
#Não pode passar () na área do telefone, somente numeros

# cursor.execute('DELETE FROM usuario WHERE id=1')

    #Depois de fazer o código SQL temos que dar o comando em python para mostrar os dados
# dados = cursor.execute('SELECT * FROM usuario')
# for usuario in dados: 
#     print(usuario)
# Note! você pode dar qualquer nome em item 

# cursor.execute('UPDATE usuario SET endereco="Curitiba" WHERE nome="Joana" ')
# dados = cursor.execute('SELECT * FROM usuario ORDER BY telefone DESC')

# dados = cursor.execute('SELECT DISTINCT * FROM usuario')

# dados = cursor.execute('SELECT id, nome FROM usuario GROUP BY nome  HAVING id > 2')

#--------------------------------------------------------------------------------------
# cursor.execute(
#     'CREATE TABLE gerentes( id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# cursor.execute(
#     "INSERT INTO gerentes(id, nome, endereco, email) VALUES(1, 'Isadora', 'Salvador', 'isa@gmail.com')")

# cursor.execute("INSERT INTO gerentes(id, nome, endereco, email) VALUES(8, 'Inglaterra', 'Sao Paulo', 'cyt@gmail.com')")

#INNER JOIN
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

#LEFT JOIN
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

#RIGHT JOIN
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

#FULL JOIN
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id = gerentes.id')

#SUBCONSULTAS
dados = cursor.execute('SELECT * FROM usuario WHERE id IN (SELECT id FROM gerentes )')
#NOTE! É um comando dentro de outro comando
for item in dados: 
    print(item)


#As informações só serão enviadas pro banco quando chegar nessa função commit
conexao.commit()
#Sempre fechar a conexão para não dar conflitos com algum outro BD que vc esteja mexendo
conexao.close()