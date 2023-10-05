#Classe madre Utente
class Utente:
    
    #Costruttore
    def __init__(self,nome,cognome,anno):
        self.__nome = nome
        self.__cognome = cognome
        self.__anno = anno  
      
    #Metodi Setter
    def setNome(self,nome):
        self.__nome = nome
    def setCognome(self,cognome):
        self.__cognome = cognome
    def setAnno(self,anno):
        self.__anno = anno
        
    #Metodi Getter
    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def getAnno(self):
        return self.__anno
    
    #ToString
    def __str__(self):
        return 'Nome: ' + self.__nome + '\nCognome: ' + self.__cognome + '\nAnno: ' + self.__anno + '\n'

