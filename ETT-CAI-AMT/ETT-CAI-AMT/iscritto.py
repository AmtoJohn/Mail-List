# Importo la Classe Utente
from utente import Utente


# Creao la Classe Guest che eredita da Utente
class Guest(Utente):

    # Costruttore
    def __init__(self, nome, cognome, anno, tipo, doc):
        Utente.__init__(self, nome, cognome, anno)
        self.__tipo = tipo
        self.__doc = doc

    # Metodi Setter
    def setTipo(self, tipo):
        self.__tipo = tipo

    def setDoc(self, doc):
        self.__doc = doc

    # Metodi Getter
    def getTipo(self):
        return self.__tipo

    def getDoc(self):
        return self.__doc

    # ToString
    def __str__(self):
        Utente.__str__(self) + '\nTipo: ' + self.__tipo + '\nDoc: ' + self.__doc + '\n'


# Creazione Classe Studente
class Studente(Utente):

    # Costruttore
    def __init__(self, nome, cognome, anno, matricola, corso):
        Utente.__init__(self, nome, cognome, anno)
        self.__matricola = matricola
        self.__corso = corso

    # Metodi Setter
    def setMatricola(self, matricola):
        self.__matricola = matricola

    def setCorso(self, corso):
        self.__corso = corso

    # Metodi Getter
    def getMatricola(self):
        return self.__matricola

    def getCorso(self):
        return self.__corso

    # ToString
    def __str__(self):
        Utente.__str__(self) + '\nMatricola: ' + self.__matricola + '\nCorso: ' + self.__corso + '\n'


# Creazione Classe Docente
class Docente(Utente):
    def __init__(self, nome, cognome, anno, cf, dip):
        Utente.__init__(self, nome, cognome, anno)
        self.__cf = cf
        self.__dip = dip

    # Metodi Setter
    def setCF(self, cf):
        self.__cf = cf

    def setDip(self, dip):
        self.__dip = dip

    # Metodi Getter
    def getCF(self):
        return self.__cf

    def getDip(self):
        return self.__dip

    # ToString
    def __str__(self):
        Utente.__str__(self) + '\nCF: ' + self.__cf + '\nDip: ' + self.__dip + '\n'
