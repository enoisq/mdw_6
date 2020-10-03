import sqlite3
import json
from time import gmtime, strftime



def armazena_dados(dados):
    print ("\\\\**********Módulo de Gerenciamento de Dados\\\\******")
    print ("Processando os dados")
    print ("Armazenando os Dados no BD")
    data=strftime("%Y-%m-%d %H:%M:%S")
    dados['time']=data
    conn = sqlite3.connect('/usr/bin/mdw_6/json.db')
    c = conn.cursor()
    c.execute("INSERT INTO medidas('time', 'dados') VALUES (?,?)",(data,str(dados)))
    conn.commit()











