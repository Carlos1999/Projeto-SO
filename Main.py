from disco import Disco
from memoriaFisica import Memoria 
from memoriaVirtual import MemoriaVirtual 
import time
import threading
import sys

memoriaVirtual = MemoriaVirtual(4)
disco = Disco('arquivo.txt')
retirarProcesso = 0
prioridade = 4
contadorPrioridade = 0

def controlaTempoPrioridade():
  global contadorPrioridade
  global prioridade
  while(True):
    if(t2.isAlive()):
      if(prioridade == 4):
        if(contadorPrioridade==15):
          prioridade = 3
          print("Prioridade mudou para:"+str(prioridade))
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          memoriaVirtual.controleTempoBitR()
          time.sleep(1)

      elif(prioridade == 3):
        if(contadorPrioridade==10):
          prioridade = 2
          print("Prioridade mudou para:"+str(prioridade))
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          memoriaVirtual.controleTempoBitR()
          time.sleep(1)

      elif(prioridade == 2):
        if(contadorPrioridade== 8):
          prioridade = 1
          print("Prioridade mudou para:"+str(prioridade))
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          memoriaVirtual.controleTempoBitR()
          time.sleep(1)

      elif(prioridade == 1):
        if(contadorPrioridade==5):
          prioridade = 4
          print("Prioridade mudou para:"+str(prioridade))
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          memoriaVirtual.controleTempoBitR()
          time.sleep(1)  

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
            if(processo == [0,"Defalt",0,0,0]):
              continue
            elif(processo[2]==0):
              print("Processo ",processo," finalizou a execução! (não volta para o disco)")
            else:
              disco.escreverProcessoDisco(str(processo[0])+";"+processo[1]+";"+str(processo[2])+";"+str(processo[3])+";"+str(processo[4]),False)
        print("Memoria virtual:\nBitR|Tempo|Índice|Processo")
        memoriaVirtual.printMemoriaVirtual()
        print("Memoria fisica:\nMapa De Bits|Inicio|Fim|Processo")
        memoriaVirtual.printMemoriaFisica()   
        print("--------------------------------------------------------------")
        retirarProcesso -= 1
        time.sleep(1)
      if(t3.isAlive() == False):
        sys.exit(0) 

def CPU():
    global retirarProcesso
    global prioridade
    global contadorPrioridade
    processoFinalizou =0
    encontrouProcesso = 0
    while(True):
      if(memoriaVirtual.cheia()):      
        for processo in memoriaVirtual.getProcessos():
          if(processo[3][3]==prioridade and processo[3][2]!=0):
            memoriaVirtual.decrementaProcesso(processo)
            print("Executando Processo:",processo[3])           
            time.sleep(1)
            encontrouProcesso = 1
            break

        for processo in memoriaVirtual.getProcessos():            
          if(processo[3][2]==0):
            processoFinalizou +=1

        if(disco.vazio() and processoFinalizou == len(memoriaVirtual.getProcessos())):
          print("cabo")
          disco.escreverProcessoDisco("1;a;3;4;500",False)
          disco.escreverProcessoDisco("2;b;3;4;500",False)
          disco.escreverProcessoDisco("3;c;3;4;500",False)
          disco.escreverProcessoDisco("4;d;3;4;500",False)
          disco.escreverProcessoDisco("5;e;3;4;500",False)
          disco.escreverProcessoDisco("6;f;3;4;500",False)
          disco.escreverProcessoDisco("7;g;3;4;500",False)
          disco.escreverProcessoDisco("8;h;3;4;500",True)
          sys.exit(0)

        if(processoFinalizou == len(memoriaVirtual.getProcessos())):
          print("Todos os processos finalizaram, Buscando novos na memória!")
          retirarProcesso = len(memoriaVirtual.getProcessos())
          time.sleep(len(memoriaVirtual.getProcessos())+1)

        elif (encontrouProcesso==0 and prioridade>1):
          contadorPrioridade = 0
          prioridade -=1
          print("Prioridade mudou para:"+str(prioridade))

        elif (encontrouProcesso==0 and prioridade==1):
          contadorPrioridade = 0
          prioridade = 4
          print("Prioridade mudou para:"+str(prioridade))
        
        processoFinalizou =0
        encontrouProcesso = 0
        
      else:
        processoFinalizou = 0
        retirarProcesso = 1 
        time.sleep(1)    

     
t1 = threading.Thread(target=controlaTempoPrioridade)
t2 = threading.Thread(target=controlaRetidadaDisco)
t3 = threading.Thread(target=CPU)
t3.start() 
t1.start()
t2.start()
    
