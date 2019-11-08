from disco import Disco
from memoriaFisica import Memoria 
from memoriaVirtual import MemoriaVirtual 
import random
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
    if(t3.isAlive()):
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
            if(processo == [0,"VAZIO",0,-1,0]):
              continue
            elif(processo[2]==0):
              print("Processo ",processo," finalizou a execução! (não volta para o disco)")
            else:
              disco.escreverProcessoDisco(str(processo[0])+";"+processo[1]+";"+str(processo[2])+";"+str(processo[3])+";"+str(processo[4]),False)
        print("Memoria virtual:\nBitR|Tempo|Índice|Processo")
        memoriaVirtual.printMemoriaVirtual()
        print("Memoria fisica:\nMapa De Bits|Inicio|Fim|Processo")
        memoriaVirtual.printMemoriaFisica()   
        print("--------------------------------------------------------------\n \n")
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
      if(memoriaVirtual.cheia() or disco.vazio()):      
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
          print("Disco e memória vazios, programa finalizado!")
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
          for processo in memoriaVirtual.getProcessos():
            processo[3][3] = -1
          print("\n \n \n |-------------------------------------------------------------------|")              
          print("Todos os processos na memória foram executados, serão trazidos novos!")
          print("|-------------------------------------------------------------------|\n \n \n")
          prioridade = 4
          contadorPrioridade = 0
          time.sleep(1)


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

def inserirProcessos():
  while(True):
    quantidade = input("A qualquer momento digite a quantidade de processos novos que deseja criar, todos os valores dos processos serão preenchidos aleatoriamente ")
    
    for i in range (0,int(quantidade)):
      letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      pid = random.randint(0,9999)
      while (disco.existeNoDisco(str(pid))):
        pid = random.randint(0,9999)
      name = ""
      for letra in range (0,6):
        name += random.choice(letras)
      quantum = random.randint(1,4)
      priority = random.randint(1,4)
      size = random.randint(100,500)
      if(i == int(quantidade)-1):        
        disco.escreverProcessoDisco(str(pid)+";"+name+";"+str(quantum)+";"+str(priority)+";"+str(size),True)
      elif (i ==0):
        disco.escreverProcessoDisco("\n"+str(pid)+";"+name+";"+str(quantum)+";"+str(priority)+";"+str(size),False)
      else:
        disco.escreverProcessoDisco(str(pid)+";"+name+";"+str(quantum)+";"+str(priority)+";"+str(size),False) 
    time.sleep(5)

t1 = threading.Thread(target=controlaTempoPrioridade)
t2 = threading.Thread(target=controlaRetidadaDisco)
t3 = threading.Thread(target=CPU)
t4 = threading.Thread(target=inserirProcessos)

t3.start() 
t1.start()
t2.start()