# Main
# Importo da iscritto le Classi Guest, Docente e Studente
from iscritto import Guest
from iscritto import Studente
from iscritto import Docente

# Definisco costanti per le opzioni del menu
INSERISCI = 1
ELIMINA = 2
CERCA_CF = 3
CERCA_EMAIL = 4
ESCI = 5


# Metodo per visualizzare il menu e ottenere la scelta dell'utente
def menu():
    print('1) Inserisci: ')
    print('2) Elimina: ')
    print('3) Cerca CF: ')
    print('4) Cerca email: ')
    print('5) Esci: ')

    try:
        return int(input('Scelta: '))
    except ValueError:
        return -1


# Metodo per inserire un nuovo iscritto nella lista
def inserisci(iscritti):
    email = input('Email: ')

    if email in iscritti:
        print('Utente già iscritto.')
    else:
        tipo = ''

        while tipo != 'g' and tipo != 's' and tipo != 'd' and tipo != 'a':
            tipo = input('Tipo (g = Guest, s = Studente, d = Docente, a = Annulla): ')

        if tipo != 'a':
            nome = input('Nome: ')
            cognome = input('Cognome: ')
            try:
                anno = int(input('Anno: '))
            except ValueError:
                print('Anno non valido.')
                return

            if tipo == 'g':
                tipo_doc = ''
                while tipo_doc != 'p' and tipo_doc != 'c' and tipo_doc != 'a':
                    tipo_doc = input('Tipo documento (p = Passaporto, c = CI, a = Annulla): ')

                if tipo_doc == 'a':
                    return

                doc = input('Numero documento: ')

                iscritti[email] = Guest(nome, cognome, anno, tipo_doc, doc)

            elif tipo == 's':
                matricola = input('Matricola: ')
                corso = input('Corso: ')

                iscritti[email] = Studente(nome, cognome, anno, matricola, corso)

            else:
                cf = input('CF: ')

                if len(cf) != 16:
                    return

                dip = input('Dipartimento: ')

                iscritti[email] = Docente(nome, cognome, anno, cf, dip)


# Metodo per eliminare un iscritto dalla lista
def elimina(iscritti):
    email = input('Email: ')

    if email in iscritti:
        del iscritti[email]


# Metodo per cercare il CF (Codice Fiscale) di docenti di un dato dipartimento
def cerca_cf(iscritti):
    dip = input('Dipartimento: ')

    for email in iscritti:
        if isinstance(iscritti[email], Docente):
            if iscritti[email].getDip() == dip:
                print(iscritti[email].getCF())


# Metodo per cercare email di studenti in un intervallo di anni
def cerca_email(iscritti):
    try:
        anno1 = int(input('Da (incluso): '))
        anno2 = int(input('A (escluso): '))
    except ValueError:
        print('Anno non valido.')
    else:
        for email in iscritti:
            if isinstance(iscritti[email], Studente):
                if anno1 <= iscritti[email].getAnno() < anno2:
                    print(email)


# Metodo principale
def main():
    iscritti = {}  # Dizionario per memorizzare gli iscritti

    c = menu()  # Mostra il menu e ottiene la scelta dell'utente
    while c != ESCI:  # Finché l'utente non sceglie di uscire
        if c == INSERISCI:
            inserisci(iscritti)  # Chiamata alla funzione inserisci
        elif c == ELIMINA:
            elimina(iscritti)  # Chiamata alla funzione elimina
        elif c == CERCA_CF:
            cerca_cf(iscritti)  # Chiamata alla funzione cerca_cf
        elif c == CERCA_EMAIL:
            cerca_email(iscritti)  # Chiamata alla funzione cerca_email
        else:
            print('Scelta non valida.')

        c = menu()  # Mostra nuovamente il menu e ottiene la scelta dell'utente


# Esegui la funzione principale all'avvio dello script

