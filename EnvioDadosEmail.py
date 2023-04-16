#Importando bibliotecas
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector
from mysql.connector import Error
import pandas as pd

try:#Conexão dentro do Try para gerenciar o erro! 

#Conectando ao banco de dados
    con = mysql.connector.connect ( 
    host="localhost",
    user="root",
    password="zz14744",
    database="processadores_valor"
)
#Utilizando o panda para pegar o DataFrame
    table_processador = "SELECT * FROM processador_valor_data"
    processador_specs = pd.read_sql('SELECT * FROM processador_valor_data',con)
    print (processador_specs)

#Caso de erro mostre essa mensagem
except mysql.connector.Error as erro: 
 print("Falha ao pegar os dados da tabela no MySQL: {}".format(erro))

#Fechando o banco de dados
finally:
#Criando cursor
    cursor = con.cursor()
if (con.is_connected()):
    cursor.close()
    con.close()
    print ("A conexão ao MySQL foi encerrada.")

# Configurações do email
login = 'lucaszmp011@gmail.com'
password = '***********'
receiver = ['lucaszmp011@gmail.com']

#Criando função para enviar email
def send_email():
     
#Criando mensagem de email
     msg = MIMEMultipart()

#Adicionando o assunto e destinatário do email
     msg['Subject'] = 'Processadores e seus valores referente a data.'
     msg['lucaszmp011@gmail.com']

# Adicionando remetente
     msg['lucaszmp011@gmail.com']

#Criando corpo do email
     body_email = "<p><b>PROCESSADOR VALOR E INFORMAÇÕES</b></p>"\
             "<p>Segue em anexo a tabela contendo os valores dos processadores referente a data.</p>" \
             "<p>Todos os processadores e seus valores foram retirados da loja KABUM " \
             "<a href='https://www.kabum.com.br/hardware/processadores'>https://www.kabum.com.br/hardware/processadores</a>.</p>"


#Adicionando corpo ao email
     msg.attach(MIMEText(body_email,"html"))

# Criando o obejeto MIMEApplication com os dados do DataFrame
     df_bytes = processador_specs.to_csv(index=False).encode()
     attachment = MIMEApplication(df_bytes, Name = 'Table_processador.csv')
     

# Adicionando o objeto MIMEApplication como anexo ao email
     attachment['Table_processadores.csv'] 
     msg.attach(attachment)

     try: #Conexão dentro do Try para gerenciar o erro! 
         
# Conectando ao servidor do SMTP do Gmail
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()

#Login para enviar o email
         server.login(login, password)

#Enviando email
         text = msg.as_string()
         server.sendmail(login,receiver,text)
         print('Email enviado')
         server.quit()
     except Exception as error:
         print ('Error ao enviar o email', error)

#Chmando função para enviar o email
send_email()