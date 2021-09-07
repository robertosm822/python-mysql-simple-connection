import sys
import os
## recurso para importar arquivos py externos
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

## from connect_mysql import *
from oo.connet_db import ConnectionMysql

#from connect_mysql import *
## import mysql.connector

## Funciana em modo de prompt do Commander como administrador do Windows
## cnx = mysql.connector.connect(user='robertosm8222', password='87987469', host='db4free.net', database='sistema_rsm_2')

## importar variaveis de arquivo externo py - passa o nome do arquivo sem extensao
from insert import *

## cnx = ConnectionMysql()
cursor = cnx.cursor()

## recebendo parametros

number = sys.argv
name = ''

for argument in sys.argv:
    name = argument

    if name == "" or name is None:
        query = ("SELECT clientes.nome, clientes.sobrenome FROM `clientes`")
        name = ""
    else:
        query = ("SELECT clientes.nome, clientes.sobrenome FROM `clientes` where clientes.nome like '%"+name+"%'")


cursor.execute(query,name)

for (nome, sobrenome) in cursor:
  print(nome+" "+sobrenome+' '+name)
  ## +Insert("Anita", "Souza", "1980-10-25"))

cursor.close()
cnx.close()
