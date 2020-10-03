import time
import threading
import json


    

def recebe_dados():
    print ("\\\*****Módulo de Gerenciamento de Comunicação com os Dispositivos******\\\\")
    print ("Recebendo dados das tomadas")
    with open('/usr/bin/mdw_6/modules/hems_mw.json', 'r') as json_file:
        dados = json.load(json_file)
        return dados


def envia_ger_dados():
    dados_prontos = recebe_dados()
    print ("Enviando dados para o Módulo de Gerenciamento de Dados")
    return dados_prontos
    


