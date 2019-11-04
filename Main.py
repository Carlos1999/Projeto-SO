from disco import Disco
from memoriaFisica import Memoria 
from memoriaVirtual import MemoriaVirtual 
import time
import threading
import sys

memoriaVirtual = MemoriaVirtual(5)
disco = Disco('arquivo.txt')
retirarProcesso = 0
prioridade = 4
contadorPrioridade = 0
def controlaTempoBitR():
  while(True):
    if(t2.isAlive()):
      memoriaVirtual.controleTempoBitR()
      time.sleep(1) 
    else:
      sys.exit(0) #finalizar programa

def controlaTempoPrioridade():
  global contadorPrioridade
  global prioridade
  while(True):
    if(t2.isAlive()):
      if(prioridade == 4):
        if(contadorPrioridade==15):
          prioridade = 3
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          time.sleep(1)

      elif(prioridade == 3):
        if(contadorPrioridade==10):
          prioridade = 2
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          time.sleep(1)

      elif(prioridade == 2):
        if(contadorPrioridade== 8):
          prioridade = 1
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          time.sleep(1)

      elif(prioridade == 1):
        if(contadorPrioridade==5):
          prioridade = 4
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          time.sleep(1)  
      print("Prioridade:"+str(prioridade)+"Tempo:"+str(contadorPrioridade))  

    else:
      sys.exit(0) #finalizar programa

def controlaRetidadaDisco():
    global retirarProcesso
    while(True):      
      if(retirarProcesso >0):
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
        retirarProcesso -= 1
    sys.exit(0)  

def CPU():
    global retirarProcesso
    global prioridade
    while(True):
      if(memoriaVirtual.cheia()):      
        for processo in memoriaVirtual.getProcessos():
          if(processo[3]==prioridade):
           memoriaVirtual.decrementaProcesso(processo)           
           time.sleep(1)
           if(processo[2] ==0):
             processoFinalizou = True
           break

           if (prioridade>1):
             prioridade = prioridade -1
             break
           else:
             prioridade = 4
             break  
      elif(memoriaVirtual.cheia()==False or processoFinalizou ==True ):
        processoFinalizou = False
        retirarProcesso = 1    




t1 = threading.Thread(target=controlaTempoBitR)
t2 = threading.Thread(target=controlaTempoPrioridade)
t3 = threading.Thread(target=controlaRetidadaDisco)
t2.start()   