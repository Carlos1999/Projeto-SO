from disco import Disco
from memoriaFisica import Memoria 
from memoriaVirtual import MemoriaVirtual 
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random
import time
import threading
import sys

def iniciar():
  t3.start()
  t2.start()
  t1.start()

def inserirProcessos():
  quantidade = entrada.get()
  
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
  tabelaDisco.delete(*tabelaDisco.get_children())
  for item in disco.getDisco():
    tabelaDisco.insert('', 'end', values=item)


janela = tk.Tk()
janela.title("Projeto Kernel")
tamanhoMemoria = 4
memoriaVirtual = MemoriaVirtual(tamanhoMemoria)
disco = Disco("arquivo.txt")

# Memória Virtual ----------------------------------------------------

mVlabel = tk.Label(janela,text = "Memória Virtual:")
mVlabel.place(x = 20, y = 10)

dataColsVirtual = ('BITR', 'TIME', 'INDEX','PID')
tabelaVirtual = ttk.Treeview(janela,columns=dataColsVirtual ,show='headings', height = tamanhoMemoria )
tabelaVirtual.column(column = 'BITR', width = '40')
tabelaVirtual.column(column = 'TIME', width = '40')
tabelaVirtual.column(column = 'INDEX', width = '40')
tabelaVirtual.column(column = 'PID', width = '40')
tabelaVirtual.place(x = 20, y = 40)

for c in dataColsVirtual:
  tabelaVirtual.heading(c, text=c.title())

for item in memoriaVirtual.getMemoriaVirtual():
  tabelaVirtual.insert('', 'end', values=item)

#Memória Física ----------------------------------------------------------
mFlabel = tk.Label(janela,text = "Memória Física:")
mFlabel.place(x = 250, y = 10)

dataColsFisica = ('MAPA', 'START', 'END')
tabelaFisica = ttk.Treeview(janela,columns=dataColsFisica ,show='headings', height = tamanhoMemoria   )
tabelaFisica.column(column = 'MAPA', width = '40')
tabelaFisica.column(column = 'START', width = '40')
tabelaFisica.column(column = 'END', width = '40')
tabelaFisica.place(x = 250, y = 40)
for c in dataColsFisica:
  tabelaFisica.heading(c, text=c.title())

for item in memoriaVirtual.getProcessos():
  tabelaFisica.insert('', 'end', values=item)

#Tabela Processos  ----------------------------------------------------------
processlabel = tk.Label(janela,text = "Processos:")
processlabel.place(x = 372, y = 10)


dataColsProcess = ('PID', 'NAME', 'QUANTUM','PRIORITY','SIZE')
tabelaProcess = ttk.Treeview(janela,columns=dataColsProcess ,show='headings', height = tamanhoMemoria)
tabelaProcess.column(column = 'PID', width = '60')
tabelaProcess.column(column = 'NAME', width = '60')
tabelaProcess.column(column = 'QUANTUM', width = '30')
tabelaProcess.column(column = 'PRIORITY', width = '30')
tabelaProcess.column(column = 'SIZE', width = '40')
tabelaProcess.place(x = 372, y = 40)

for c in dataColsProcess:
  tabelaProcess.heading(c, text=c.title())

for item in memoriaVirtual.getProcessos():
  print(item[3])
  tabelaProcess.insert('', 'end', values=item[3])


#Tabela CPU -----------------------------------------------------------------------
CPUlabel = tk.Label(janela,text = "CPU:")
CPUlabel.place(x = 20, y = 200)




dataColsCPU = ('PID', 'NAME', 'QUANTUM','PRIORITY','SIZE')
tabelaCPU = ttk.Treeview(janela,columns=dataColsCPU ,show='headings', height = 1 )
tabelaCPU.column(column = 'PID', width = '40')
tabelaCPU.column(column = 'NAME', width = '40')
tabelaCPU.column(column = 'QUANTUM', width = '40')
tabelaCPU.column(column = 'PRIORITY', width = '40')
tabelaCPU.column(column = 'SIZE', width = '40')
tabelaCPU.place(x = 20, y = 230)

for c in dataColsCPU:
  tabelaCPU.heading(c, text=c.title())

CPU = [['PID', 'NAME', 'QUANTUM','PRIORITY','SIZE']]
for item in CPU:
  tabelaCPU.insert('', 'end', values=item)

#Tabela Disco -----------------------------------------------------------------------
discolabel = tk.Label(janela,text = "Disco:")
discolabel.place(x = 250, y = 200)

dataColsDisco = ('PID', 'NAME', 'QUANTUM','PRIORITY','SIZE')
tabelaDisco = ttk.Treeview(janela,columns=dataColsDisco ,show='headings', height = disco.tamanhoDisco())
tabelaDisco.column(column = 'PID', width = '40')
tabelaDisco.column(column = 'NAME', width = '80')
tabelaDisco.column(column = 'QUANTUM', width = '40')
tabelaDisco.column(column = 'PRIORITY', width = '40')
tabelaDisco.column(column = 'SIZE', width = '40')
tabelaDisco.place(x = 250, y = 230)

for c in dataColsDisco:
  tabelaDisco.heading(c, text=c.title())

for item in disco.getDisco():
  tabelaDisco.insert('', 'end', values=item)


#menu para inserir no disco  -----------------------------------------------------------------------
inserirLabel = tk.Label(janela,text = "Inserir processos no disco:", font = ("arial",12,"bold"))
inserirLabel.place(x = 510, y = 200)
entrada = Entry(janela)
entrada.place(x=510, y = 220)
botao = Button(janela, width = 20, text = 'inserir', command = inserirProcessos )
botao.place(x = 510, y = 260)

# menu iniciar -----------------------------------------------------------------------------
botao = Button(janela, width = 5, text = 'start', command = iniciar , bg = 'green')
botao.place(x = 510, y = 400)
#variáveis globais -----------------------------------------------------------------------

retirarProcesso = 0
prioridade = 4
contadorPrioridade = 0
var = StringVar()
priolabel = tk.Label(janela, textvariable=var)
var.set("Prioridade: 4")
priolabel.place(x = 20, y = 500)

move = StringVar()
movelabel = tk.Label(janela, textvariable=move  )
move.set("")
movelabel.place(x = 60, y = 200)


def controlaTempoPrioridade():
  global contadorPrioridade
  global prioridade
  while(True):
    if(t3.isAlive()):
      if(prioridade == 4):
        if(contadorPrioridade==15):
          prioridade = 3
          print("Prioridade mudou para:"+str(prioridade))

          var.set("Prioridade: "+str(prioridade)) 
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          memoriaVirtual.controleTempoBitR()
          time.sleep(1)

      elif(prioridade == 3):
        if(contadorPrioridade==10):
          prioridade = 2
          print("Prioridade mudou para:"+str(prioridade))
          var.set("Prioridade: "+str(prioridade))
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          memoriaVirtual.controleTempoBitR()
          time.sleep(1)

      elif(prioridade == 2):
        if(contadorPrioridade== 8):
          prioridade = 1
          print("Prioridade mudou para:"+str(prioridade))
          var.set("Prioridade: "+str(prioridade))
          contadorPrioridade = 0
        else:  
          contadorPrioridade+=1
          memoriaVirtual.controleTempoBitR()
          time.sleep(1)

      elif(prioridade == 1):
        if(contadorPrioridade==5):
          prioridade = 4
          var.set("Prioridade: "+str(prioridade))
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
        #atualizar memória virtual ---------------------------------------------------
        move.set("Processos indo do disco para a memória!")
        movelabel.config(bg = "red")
        tabelaVirtual.delete(*tabelaVirtual.get_children())
        for item in memoriaVirtual.getMemoriaVirtual():
          tabelaVirtual.insert('', 'end', values=item)

        #atualizar memória fisica ----------------------------------------------------
        tabelaFisica.delete(*tabelaFisica.get_children())
        tabelaProcess.delete(*tabelaProcess.get_children())
        for item in memoriaVirtual.getProcessos():
          tabelaFisica.insert('', 'end', values=item)
          tabelaProcess.insert('', 'end', values=item[3])

        tabelaDisco.delete(*tabelaDisco.get_children())
        for item in disco.getDisco():
          tabelaDisco.insert('', 'end', values=item)  

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
        move.set("")
        movelabel.config(bg = janela.cget("background"))
        

        for processo in memoriaVirtual.getProcessos():
          if(processo[3][3]==prioridade and processo[3][2]!=0):
            memoriaVirtual.decrementaProcesso(processo)

            tabelaCPU.delete(*tabelaCPU.get_children())
            CPU = [processo[3]]
            for item in CPU:
              tabelaCPU.insert('', 'end', values=item)  

            print("Executando Processo:",processo[3])           
            time.sleep(1)
            encontrouProcesso = 1
            if(processo[3][2]==0):
              #atualizar memória fisica ----------------------------------------------------
              tabelaFisica.delete(*tabelaFisica.get_children())
              tabelaProcess.delete(*tabelaProcess.get_children())
              for item in memoriaVirtual.getProcessos():
                tabelaFisica.insert('', 'end', values=item)
                tabelaProcess.insert('', 'end', values=item[3])

            break


        for processo in memoriaVirtual.getProcessos():            
          if(processo[3][2]==0):
            processoFinalizou +=1

        if(disco.vazio() and processoFinalizou == len(memoriaVirtual.getProcessos())):
          print("Disco e memória vazios, programa finalizado!")
          messagebox.showinfo("Programa Finalizou", "Todos os processos no disco foram executados! Fim do programa")
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

          var.set("Prioridade: "+str(prioridade)) 
          contadorPrioridade = 0
          time.sleep(1)


        elif (encontrouProcesso==0 and prioridade>1):
          contadorPrioridade = 0
          prioridade -=1
          print("Prioridade mudou para:"+str(prioridade))
          var.set("Prioridade: "+str(prioridade))

        elif (encontrouProcesso==0 and prioridade==1):
          contadorPrioridade = 0
          prioridade = 4
          var.set("Prioridade: "+str(prioridade))
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


priolabel.pack()
priolabel.place(x = 20, y = 270)

movelabel.pack()
movelabel.place(x = 250, y = 140)

janela.geometry("740x500")
janela.mainloop()
