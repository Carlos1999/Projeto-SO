from disco import Disco
from memoriaSwapping import Memoria 
from memoriaVirtual import MemoriaVirtual 
import time
import threading
import sys

memoriaVirtual = MemoriaVirtual(5)
disco = Disco('arquivo.txt')
retirarProcesso = False
prioridade = 4
def controlaTempoBitR():
  while(True):
    if(t2.isAlive()):
      memoriaVirtual.controleTempoBitR()
      time.sleep(1) 
    else:
      sys.exit(0) #finalizar programa

def controlaTempoPrioridade():
  while(True):
    if(t2.isAlive()):
      if(prioridade == 4):
        prioridade = 3
        time.sleep(15)
      if(prioridade == 3):
        prioridade = 2
        time.sleep(10)
      if(prioridade == 2):
        prioridade = 1
        time.sleep(5)
      if(prioridade == 1):
        prioridade = 4
        time.sleep(20)  
        
    else:
      sys.exit(0) #finalizar programa

def controlaRetidadaDisco():
    global retirarProcesso
    while(True):      
        dados = disco.retirarProcessoDisco()
        dados = dados.split(";")
        processosRetirados = memoriaVirtual.organizarProcesso(int(dados[0]),dados[1],int(dados[2]),int(dados[3]),int(dados[4]))             
        for processo in processosRetirados:
            if(processo!= [0,0,0,0,0]):
                disco.escreverProcessoDisco(str(processo[0])+";"+processo[1]+";"+str(processo[2])+";"+str(processo[3])+";"+str(processo[4]))
        print("Memoria virtual:\nBitR|Tempo|Índice|Processo")
        memoriaVirtual.printMemoriaVirtual()
        print("Memoria fisica:\nMapa De Bits|Inicio|Fim|Processo")
        memoriaVirtual.printMemoriaFisica()   
        print("--------------------------------------------------------------")
        while(retirarProcesso ==False and memoriaVirtual.vazia() == False):
            time.sleep(1) 
        time.sleep(2) 

    sys.exit(0)  

def CPU():
    global retirarProcesso
    global prioridade 
    while (True):



t1 = threading.Thread(target=controlaTempoBitR)
t2 = threading.Thread(target=controlaRetidadaDisco)
t2.start()   
time.sleep(0.5) 
t1.start()