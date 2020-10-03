from modules import *
import random
import time
import threading
import json
import sys
import schedule

print ("\\\\Middleware em execução/////")


def recebe():
        dados.armazena_dados(comunicacao_dispositivos.envia_ger_dados())

   
def inicio():
        try:                      
                
                schedule.every(1).seconds.do(recebe).tag('mdw')
                schedule.every(5).seconds.do(comunicacao_aplicacao.envia_nuvem,1).tag('mdw')
                
                
        except KeyboardInterrupt:
            sys.exit()    
            print ( "Middleware encerrado" )
            
        while True:
                try:
                        schedule.run_pending()
                        time.sleep(0.5)

                except Exception as e:   
                        print ( "rodando ainda" + str(e) )
                        pass
                except KeyboardInterrupt:
                        sys.exit()    
                        print ( "Middleware encerrado" )
            

inicio()
