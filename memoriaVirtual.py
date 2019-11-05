from memoriaFisica   import Memoria 
from datetime import datetime

class MemoriaVirtual:
  def __init__(self,tamanhoMemoria):
    self.memoriaFisica = Memoria()
    self.tamanhoMemoria = tamanhoMemoria
    self.memoriaVirtual = [] 
    self.contador=0
    self.ponteiro=0
    for i in range(0,tamanhoMemoria):
      self.memoriaFisica.adicionarProcesso(str(i)+";NAME;1;0;"+str(int((self.memoriaFisica.getTamanhoMemoria()+1)/self.tamanhoMemoria)))
    for i in range(0,tamanhoMemoria):
      self.memoriaFisica.substituirProcesso(i,[0,"Defalt",0,0,0])  
      self.inserir([-1,0,0,0,0]) 
    
#----------------------------------------------------------------------------------
  def organizarProcesso(self,pid,name,quantum,priority,size):
    processo=[int(pid),name,int(quantum),int(priority),int(size)] 
    tamanhoMaxPagina = int((self.memoriaFisica.getTamanhoMemoria()+1)/self.tamanhoMemoria)
    processosRemovidos=[]
    
    while(processo[4]>tamanhoMaxPagina):
      processosRemovidos.append(self.inserir([processo[0],processo[1],processo[2],processo[3],tamanhoMaxPagina]))
      processo[4] = processo[4]-tamanhoMaxPagina    
    
    if(processo[4]>0):  
      processosRemovidos.append(self.inserir(processo))
    return processosRemovidos

    
  def inserir(self,processo):
    now = datetime.now()
    pagina = [1,now.second,self.contador%self.tamanhoMemoria,processo]

    if(len(self.memoriaVirtual)<self.tamanhoMemoria):
      pagina[3] = pagina[3][0]
      self.memoriaVirtual.append(pagina)
      self.contador+=1 
      return  [0,0,0,0,0]
    else:
      return self.substituicao(pagina)

  def substituicao(self,pagina):

    while (True):
      if(self.memoriaVirtual[self.ponteiro%self.tamanhoMemoria][0]==0):
        
        self.memoriaVirtual.pop(self.ponteiro%self.tamanhoMemoria)
        processoSaiu = self.memoriaFisica.substituirProcesso(self.contador%self.tamanhoMemoria,pagina[3])        
        print("Processo: ",pagina[3],"inserido na memória")
        pagina[3] = pagina[3][0]
        self.memoriaVirtual.insert(self.ponteiro%self.tamanhoMemoria,pagina)        
        self.contador+=1 
        self.ponteiro+=1 #O self.ponteiro deve andar sempre que a página mais antiga for trocada
        
      
        break
      else:
        self.memoriaVirtual[self.ponteiro%self.tamanhoMemoria][0]=0
        self.ponteiro+=1#Se a página mais antiga ainda foi referenciada, zera o bitR e anda o ponteiro   
    return processoSaiu
#--------------------------------------------------------------------------------------------------
  def printMemoriaVirtual(self):
    for i in self.memoriaVirtual:
      print(i)      
      
  def printMemoriaFisica(self):
    self.memoriaFisica.print()

  def controleTempoBitR(self):
    now = datetime.now()
    for i in self.memoriaVirtual:
      segundosAgora = now.second
      if i[1]>= 55 and i[1] < 60:
        if abs(segundosAgora-i[1]) <= 55 and i[0] == 1:
          i[0] = 0
      else:
          if abs(segundosAgora-i[1]) >= 5 and i[0] == 1:
            i[0] = 0

  def vazia(self):
    contador =0
    for pagina in self.memoriaVirtual:
      print(pagina)
      if(pagina[3] == -1):
        contador +=1 
    if(contador == self.tamanhoMemoria):
      return True
    return False              

  def cheia(self):
    contador =0
    for pagina in self.memoriaVirtual:
      if(pagina[3] != -1):
        contador +=1 
    if(contador == self.tamanhoMemoria):
      return True
    return False    

  def esvazearMemorias(self):
    for i in range(0,len(self.memoriaVirtual)):
      self.memoriaVirtual[i][0]=0
      self.memoriaVirtual[i][3]=0
    self.memoriaFisica.esvazear()  

  def getProcessos(self):
    return self.memoriaFisica.getMemoria()

  def decrementaProcesso(self,processoParametro):
    for processo in self.memoriaFisica.getMemoria():
      if(processo==processoParametro):
        if(processo[3][2]>0):
          processo[3][2]=processo[3][2]-1
          return processo[3]            
