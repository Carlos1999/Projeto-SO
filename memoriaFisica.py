class Memoria:
  def __init__(self):
    self.tamanhoMemoria = 1999 #Kilo Bites      
    memoria = [[0,0,self.tamanhoMemoria,[]]]  
    self.memoria = memoria

  def adicionarProcesso(self,dados):
    
    dadosSplit = dados.split(";")
    processo=[int("0"+dadosSplit[0]),dadosSplit[1],int("0"+dadosSplit[2]),int(dadosSplit[3]),int(dadosSplit[4])] 
        
    contador = 0
    for espaco in self.memoria:
      if((espaco[0]==0) and espaco[2]-espaco[1]+1 >= processo[4]):
        espaco[0]=1
        espaco[2]= processo[4] + espaco[1]-1
        espaco[3]=(processo)                
        if((len(self.memoria)==contador+1) and self.memoria[contador][2]<self.tamanhoMemoria):
          self.memoria.insert(contador+1,[0,espaco[2]+1,self.tamanhoMemoria,[0,0,0,0,0]])
        return True
      contador+=1
    return False    
  
  def substituirProcesso(self,indice,processo):
    processoSaiu = self.memoria[indice][3]
    if(processo== [0,0,0,0,0]):
      self.memoria[indice][0]=0        
    else:         
      self.memoria[indice][0]=1
    self.memoria[indice][3] = processo
    return processoSaiu  
  
  def print(self):
    for espaco in self.memoria:
      print(espaco)    

  def getTamanhoMemoria(self):
    return self.tamanhoMemoria

  def getMemoria(self):
    return self.memoria  