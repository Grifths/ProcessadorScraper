#Importando biblioteca MySql
import mysql.connector

try: #Conexão dentro do Try para gerenciar o erro! 
   
   #Criando conexão ao banco de dados
   con = mysql.connector.connect ( 
    host="localhost",
    user="root",
    password="zz14744",
    database="processadores_valor"
)
   
   #Declaração SQL a ser executada
   create_table_SQL_processador = """ 
                                 CREATE TABLE processador_valor_data(
                                 idProcessador INT(15) NOT NULL AUTO_INCREMENT,
                                 NomeProcessador VARCHAR(200) NOT NULL,
                                 preco VARCHAR(20) NOT NULL,
                                 Data DATE NOT NULL,
                                 PRIMARY KEY (idProcessador))
                                 """
   
   #Criando cursor e executando SQL no banco de dados
   cursor = con.cursor()
   cursor.execute(create_table_SQL_processador)
   print("Tabela criada com sucesso!")

#Caso de erro mostre essa mensagem
except mysql.connector.Error as erro: 
  print("Falha ao criar tabela no MySQL: {}".format(erro))

 #Fechando o banco de dados
finally:
 if (con.is_connected()):
    cursor.close()
    con.close()
    print ("A conexão ao MySQL foi encerrada.")

