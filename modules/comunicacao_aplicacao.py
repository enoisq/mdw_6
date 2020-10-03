
import random
import time
import json
import sqlite3
import os
import asyncio

from azure.iot.device import IoTHubDeviceClient, Message


def busca_dados():
    print ("\\\**********Módulo de Gerenciamento de Comunicação com Aplicações********\\\\")
    print ("Buscando dados no banco de dados")

    conn = sqlite3.connect('/usr/bin/mdw_6/json.db')
    c = conn.cursor()
    c.execute("SELECT dados from medidas order by id desc limit 1")
    dados = c.fetchall()
    conn.commit()
    #print(dados)

    ndado = str(dados).replace("'","\"")
    djson = (str(ndado)[3:-4])
    #print(djson)
    jsonpronto = json.loads(djson)
     
    return jsonpronto



def reenviar(dados):
    print("Gravando informações de dados não enviados")
    timestamp=dados['time']
    s1=("/usr/bin/mdw_6/log_comunicacao_aplicacao.txt")
    S = open(s1, 'a')
    S.write(str(timestamp)+"\n")
    S.close()

    

    #dadosj = json.dumps(dados)
    #print(dadosj[0]['time'])
    #print(time)
    #print (str(dados))
    #s1=("log_comunicacao_aplicacao.json")
    #S = open(s1, 'w')
    #S.write(str(j)[3:-4])
    #S.close()

    #d = open('log_comunicacao_aplicacao.json','r') #abre arquivo json para leitura
    #js = json.load(d)
    #print (js['time'])
    #print (js['outlets'])
    #d.close()
    
def envia_iothub(dados):
    flag= 2
    #CONNECTION_STRING = "HostName=mdwcopel.azure-devices.net;DeviceId=pythondevice;SharedAccessKey=PzCUFs423r12S9qGKOu74hqwRYR+2LlOCGAssUYv9Fo="
    #CONNECTION_STRING = "HostName=HemsHub.azure-devices.net;DeviceId=Hemsd;SharedAccessKey=L3YBChE5GvupNPT2ILsQbpU58Du71yEeEmohUFeiBWE="

    try:
        with open('/etc/iotedge/config.yaml', 'r') as searchfile:
            for line in searchfile:
                if 'device_connection_string' in line:
                    string_teste = line.partition("device_connection_string: ")[2]
                    #print (string_teste)
        string_teste = string_teste.replace("\"", "")
        CONNECTION_STRING = string_teste            
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        client.connect()   
        #print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        # Send the message.
        print( "Enviando mensagem para IoTHub: "+str(dados) )
        client.send_message(str(dados))
        print ( "Enviada com sucesso!" )
        time.sleep(1)
        client.disconnect()
        flag=2

        

    except Exception as e:
        
        print ( "IoTHubClient sample stopped" )
        reenviar(dados)
        return flag
        
    

    return flag

def envia_nuvem (metodo):
    
    if (metodo==1):
        if(envia_iothub(busca_dados()))==2:
            print ("Enviando dados para a Nuvem: IoTHub")
        
            
    
    

try:
    #CONNECTION_STRING = "ostName=mdwcopel.azure-devices.net;DeviceId=pythondevice;SharedAccessKey=PzCUFs423r12S9qGKOu74hqwRYR+2LlOCGAssUYv9Fo="
    #CONNECTION_STRING = "HostName=HemsHub.azure-devices.net;DeviceId=Hemsd;SharedAccessKey=L3YBChE5GvupNPT2ILsQbpU58Du71yEeEmohUFeiBWE="
    with open('/etc/iotedge/config.yaml', 'r') as searchfile:
        for line in searchfile:
            if 'device_connection_string' in line:
                string_teste = line.partition("device_connection_string: ")[2]
                #print (string_teste)
    string_teste = string_teste.replace("\"", "")            
    CONNECTION_STRING = string_teste    
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

except:
    print ('ignoring failed address lookup')
    pass

    
