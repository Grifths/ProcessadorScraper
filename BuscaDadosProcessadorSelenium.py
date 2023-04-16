#Importando biblioteca Selenium 

from selenium import webdriver
from time import sleep
from datetime import datetime
from main import *

#Informando o navegador que irei utilizar
browser = webdriver.Chrome()

#Acessando o site que irei extrair os dados
browser.get("https://www.kabum.com.br/hardware/processadores")

sleep(3)

#Declarando variáveis para receber os nomes,valores e data
PRICE = []
NAME = []
DATE = []
DATE_PT = datetime.now().strftime('%Y/%m/%d')


#Criando Função Name e Value
def FindElementName(X,A):
    element_name = browser.find_element(X,A)
    return element_name

def FindElementeValue(X,A1):
    element_value = browser.find_element(X,A1)
    return element_value

#Busca dos dados
for name,value in zip(names,values):
 element_name = browser.find_element(X,name)
 element_value = browser.find_element(X,value)
 PRICE.append(element_value.text)
 NAME.append(element_name.text)
 DATE.append(DATE_PT)

#Acessando o site que irar extrair os dados
browser.get("https://www.kabum.com.br/hardware/processadores?page_number=2&page_size=20&facet_filters=&sort=most_searched")
