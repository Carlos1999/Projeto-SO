class Disco:
  def __init__(self,nomeArquivo):
    self.nomeArquivo = nomeArquivo

  def retirarProcessoDisco(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')

    linhasFinal = "" 
    retornarLinha = ""
    contador = 0
    for linha in arquivoLeitura:      
      if(contador==0):  
        retornarLinha = linha
      else:
        linhasFinal += linha 
      contador += 1     
    arquivoLeitura.close()
    
    arquivoEscrita = open(self.nomeArquivo, 'w')
    arquivoEscrita.write(linhasFinal)
    arquivoEscrita.close()      
    return retornarLinha.replace("\n","")
  def existeNoDisco(self,pid):
    arquivoLeitura = open(self.nomeArquivo, 'r') 
    for linha in arquivoLeitura:
      linhaSplit = linha.split(";")       
      if(pid==linhaSplit[0]):
        arquivoLeitura.close() 
        return True
    arquivoLeitura.close()     
    return False         

  def escreverProcessoDisco(self,processo,ultimo):
    arquivoEscrita = open(self.nomeArquivo, 'a')
    processoSplit = processo.split(";")      
    if(ultimo==True):
      arquivoEscrita.write(processoSplit[0]+";"+processoSplit[1]+";"+processoSplit[2]+";"+processoSplit[3]+";"+processoSplit[4]) 
    else:
      arquivoEscrita.write(processoSplit[0]+";"+processoSplit[1]+";"+processoSplit[2]+";"+processoSplit[3]+";"+processoSplit[4]+"\n")
    print("Processo: "+processo+" foi para o disco!")
    arquivoEscrita.close()    
  
  def vazio(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')  
    conteudo = ""
    for i in arquivoLeitura:
      conteudo+=i
    
    if(conteudo==""):
      arquivoLeitura.close()
      print(conteudo)
      return True      
    arquivoLeitura.close() 
    return False  
     
  def getDisco(self):
    listaDisco = []
    arquivoLeitura = open(self.nomeArquivo, 'r') 
    for linha in arquivoLeitura:
      linhaSplit = linha.split(";")       
      listaDisco.append([linhaSplit[0],linhaSplit[1],linhaSplit[2],linhaSplit[3],linhaSplit[4]])    
    arquivoLeitura.close()
    return listaDisco       

  def tamanhoDisco(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')
    tamanho = 0
    for linha in arquivoLeitura:
      tamanho +=1
    arquivoLeitura.close()
    return tamanho

  def print(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')  
    for linha in arquivoLeitura:
        print(linha)  
    arquivoLeitura.close()  
