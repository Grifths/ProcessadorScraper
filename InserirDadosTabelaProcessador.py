#importando Biblioteca MySQL e funções do DadosSelenium
import mysql.connector
from mysql.connector import Error
from BuscaDadosProcessadorSelenium import NAME,PRICE,DATE

#criando conexão com o banco de dados

try: #Conexão dentro do Try para gerenciar o erro! 

    con = mysql.connector.connect ( 
    host="localhost",
    user="root",
    password="zz14744",
    database="processadores_valor"
)

    insert_data = """
                    INSERT INTO processador_valor_data 
                    (idProcessador,NomeProcessador,preco,Data)
                    VALUES (%s,%s,%s,%s)"""
    
    #Criando cursor
    cursor = con.cursor()

    #Gerando IDs para cada processador
    IDS = []

    cursor.execute('SELECT idProcessador FROM processador_valor_data')
    get_ids_processador = cursor.fetchall()

    list_of_ids_processador = [int(item[0]) for item in get_ids_processador]

    accountant = 1
    if len(list_of_ids_processador) > 0:
     accountant = list_of_ids_processador[-1]
    for i in NAME:
      accountant += 1
      Id = f'{accountant :02d}'
      IDS.append(Id)

    #Zipando as 3 variaveis em uma para melhor inserção no banco de dados
    DATA = tuple(zip(IDS, NAME, PRICE, DATE))
    print(DATA)

    #Executando a consulta SQL com a lista de tuplas
    cursor.executemany(insert_data,DATA)
    con.commit()
    print("Dados inseridos com sucesso! ")

#Caso de erro aqui irá mostrar o erro 
except mysql.connector.Error as e: 
    print("Falha ao inserir os dados na tabela no MySQL: {}".format(e))

finally: #Fechando o banco de dados
 if (con.is_connected()):
    cursor.close()
    con.close()
    print ("A conexão ao MySQL foi encerrada.")
