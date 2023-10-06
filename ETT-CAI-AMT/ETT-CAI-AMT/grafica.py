from tkinter import Frame, Button, END
import tkinter as tk
import main
# Amto Ettore Cai N1

class Applicazione:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail List - Menu")
        self.m = main  # istanziamo il main
        self.iscritti = {}  # Dizionario per memorizzare gli iscritti

        self.f1 = tk.Frame(self.root)
        self.f1.pack()

        # Frame
        self.f1 = Frame(self.root)
        self.f1.pack(pady=10, padx=20)

        #                               Cinque bottoni iniziali
        # Creazione Bottone Inserisci
        self.btnInserisci = Button(self.f1, text="Inserisci", command=self.apriInserisci)
        self.btnInserisci.grid(column=1, row=1)
        self.btnInserisci.configure(pady=10, padx=5, font=('Helvetica', 15), width=20, height=2)

        # Elimina
        self.btnElimina = Button(self.f1, text="Elimina", command=self.apriElimina)
        self.btnElimina.grid(column=1, row=2)
        self.btnElimina.configure(pady=10, padx=5, font=('Helvetica', 15), width=20, height=2)

        # Cerca Codice fiscale
        self.btnCercaCF = Button(self.f1, text="Cerca CF", command=self.apriCercaCF)
        self.btnCercaCF.grid(column=1, row=3)
        self.btnCercaCF.configure(pady=10, padx=5, font=('Helvetica', 15), width=20, height=2)

        # Cerca email
        self.btnCercaEmail = Button(self.f1, text="Cerca Email", command=self.apriCercaEmail)
        self.btnCercaEmail.grid(column=1, row=4)
        self.btnCercaEmail.configure(pady=10, padx=5, font=('Helvetica', 15), width=20, height=2)

        # Esci
        self.btnEsci = Button(self.f1, text="Esci", command=self.esci)
        self.btnEsci.grid(column=1, row=5)
        self.btnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=20, height=2, background="red",
                               foreground="white")

    #                                   Inizio Della Finestra Inserisci
    def apriInserisci(self):
        # Creazione finestra inserisci + titolo
        finestra_inserisci = tk.Toplevel(self.root)
        finestra_inserisci.title("Inserimento")

        # Creazione Bottone ApriGuest
        btnGuest = Button(finestra_inserisci, text="Guest", command=self.guest)
        btnGuest.grid(column=0, row=0)
        btnGuest.configure(font=("Arial", 16), fg="blue", bg="yellow", pady=10, padx=5,  width=20, height=2)

        # Creazione Bottone ApriStudenti
        btnStudenti = Button(finestra_inserisci, text="Studente", command=self.studenti)
        btnStudenti.grid(column=0, row=1)
        btnStudenti.configure(font=("Arial", 16), fg="blue", bg="yellow", pady=10, padx=5,  width=20, height=2)

        # Creazione Bottone ApriDocente
        btnDocente = Button(finestra_inserisci, text="Docente", command=self.docente)
        btnDocente.grid(column=0, row=2)
        btnDocente.configure(font=("Arial", 16), fg="blue", bg="yellow", pady=10, padx=5,  width=20, height=2)

        # Creazione Bottone ApriEsci
        btnEsci = tk.Button(finestra_inserisci, text="Exit", command=finestra_inserisci.destroy)
        btnEsci.grid(column=0, row=3)
        btnEsci.configure(font=("Arial", 16), fg="white", bg="red", pady=10, padx=5,  width=20, height=2)

    # Quando clicchi il bottone viene creata la finestra Guest
    def guest(self):
        finestra_Guest = tk.Toplevel(self.root)
        finestra_Guest.title("Inserimento | Guest")
        # vediamo se toglierlo poi
        #frame1 = Frame(finestra_Guest)
        #frame1.pack()
        #
        #lblEmail = tk.Label(frame1, text="Email", font=("Arial", 16), fg="blue")
        #lblEmail.grid(column=0, row=0)
        #eEmail = tk.Entry(frame1, width=30)
        #eEmail.grid(column=1, row=0)
        #btnAggMail = tk.Button(frame1, text="Aggiungi")
        #btnAggMail.grid(column=2, row=0)
        #btnAggMail.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

        frame2 = Frame(finestra_Guest)
        frame2.pack()

        # Crea e posiziona le label e i textbox
        labels = ["Email", "Nome", "Cognome", "Anno", "Doc"]
        self.textboxes_guest = []

        for i, label_text in enumerate(labels):
            lbl = tk.Label(frame2, text=label_text, font=("Arial", 16), fg="blue")
            lbl.grid(column=1, row=i * 50 + 10)

            textbox = tk.Entry(frame2, width=30)
            textbox.grid(column=50, row=i * 50 + 10)

            self.textboxes_guest.append(textbox)

        # Crea un bottone "Exit" nella finestra
        BtnEsci = tk.Button(frame2, text="Exit", command=finestra_Guest.destroy)
        BtnEsci.grid(column=50, row=250)
        BtnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

        # Crea un pulsante "Salva" per salvare il testo dei textbox
        btnSalvaG = tk.Button(frame2, text="Salva", command=self.salvaGuest)
        btnSalvaG.grid(column=55, row=250)
        btnSalvaG.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    def salvaGuest(self):
        contenuto_caselle = []
        labels = ["Email", "Nome", "Cognome", "Anno", "Doc"]
        for i, textbox in enumerate(self.textboxes_guest):
            testo_inserito = textbox.get()
            contenuto_caselle.append(f"{labels[i]} [{testo_inserito}]")

        mail = contenuto_caselle[0]
        print("Contenuto delle caselle Guest:")
        for item in contenuto_caselle:
            print(item)


        #self.iscritti[mail

    # Creazione finestra studenti
    def studenti(self):
        finestra_studenti = tk.Toplevel(self.root)
        finestra_studenti.title("Inserimento | Studente")

        # Crea e posiziona le label e i textbox per gli studenti
        labels = ["Nome", "Cognome", "Anno", "Matricola", "Corso", "Email"]
        self.textboxes_studenti = []

        for i, label_text in enumerate(labels):
            lbl = tk.Label(finestra_studenti, text=label_text, font=("Arial", 16), fg="blue")
            lbl.grid(column=1, row=i * 50 + 10)

            textbox = tk.Entry(finestra_studenti, width=30)
            textbox.grid(column=50, row=i * 50 + 10)

            self.textboxes_studenti.append(textbox)

        # Crea un bottone "Exit" nella finestra
        btnEsci = tk.Button(finestra_studenti, text="Exit", command=finestra_studenti.destroy)
        btnEsci.grid(column=50, row=250)
        btnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

        # Crea un pulsante "Salva" per salvare il testo dei textbox per gli studenti
        btnSalvaS = tk.Button(finestra_studenti, text="Salva", command=self.salvaStudente)
        btnSalvaS.grid(column=55, row=250)
        btnSalvaS.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

        # Funzione per salvare il testo dei textbox per gli studenti

    def salvaStudente(self):
        contenuto_caselle = []
        labels = ["Nome", "Cognome", "Anno", "Matricola", "Corso", "Email"]
        for i, textbox in enumerate(self.textboxes_studenti):
            testo_inserito = textbox.get()
            contenuto_caselle.append(f"{labels[i]} [{testo_inserito}]")

        print("Contenuto delle caselle Studente:")
        for item in contenuto_caselle:
            print(item)

    # Creazione finestra professori
    def docente(self):
        finestra_docente = tk.Toplevel(self.root)
        finestra_docente.title("Inserimento | Docente")

        # Crea e posiziona le label e i textbox per i professori
        labels = ["Nome", "Cognome", "Anno", "CodFis", "Facoltà", "Email"]
        self.textboxes_docente = []

        for i, label_text in enumerate(labels):
            lbl = tk.Label(finestra_docente, text=label_text, font=("Arial", 16), fg="blue")
            lbl.grid(column=1, row=i * 50 + 10)

            textbox = tk.Entry(finestra_docente, width=30)
            textbox.grid(column=50, row=i * 50 + 10)

            self.textboxes_docente.append(textbox)

        # Crea un bottone "Exit" nella finestra
        btnEsci = tk.Button(finestra_docente, text="Exit", command=finestra_docente.destroy)
        btnEsci.grid(column=50, row=250)
        btnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

        # Crea un pulsante "Salva" per salvare il testo dei textbox per i professori
        btnSalvaD = tk.Button(finestra_docente, text="Salva", command=self.salvaDocente)
        btnSalvaD.grid(column=55, row=250)
        btnSalvaD.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    # Funzione per salvare il testo dei textbox per i professori
    def salvaDocente(self):
        contenuto_caselle = []
        labels = ["Nome", "Cognome", "Anno", "Cod Fis", "Facoltà", "Email"]
        for i, textbox in enumerate(self.textboxes_docente):
            testo_inserito = textbox.get()
            contenuto_caselle.append(f"{labels[i]} [{testo_inserito}]")

        print("Contenuto delle caselle Docente:")
        for item in contenuto_caselle:
            print(item)

    #                                   Fine Della Finestra Inserisci

    #                                   Inizio Della Finestra Elimina
    def apriElimina(self):
        finestra_Elimina = tk.Toplevel(self.root)
        finestra_Elimina.title("Elimina")

        lblMail = tk.Label(finestra_Elimina, text="Inserisci Email", font=("Arial", 16), fg="blue", bg="yellow")
        lblMail.grid(column=0, row=0)

        self.eEmail = tk.Entry(finestra_Elimina, width=30)
        self.eEmail.grid(column=1, row=0)

        # Crea un bottone per eliminare l'utente
        btnElimina = Button(finestra_Elimina, text="Elimina", command=self.elimina)
        btnElimina.grid(column=2, row=0)
        btnElimina.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1)

        btnExit = tk.Button(finestra_Elimina, text="Exit", command=finestra_Elimina.destroy)
        btnExit.grid(column=3, row=0)
        btnExit.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="white", bg="red")

    #                                   Fine Della Finestra Elimina

    #                                   Inizio Della Finestra Cerca Codice Fiscale
    def apriCercaCF(self):
        finestra_CercaCF = tk.Toplevel(self.root)
        finestra_CercaCF.title("Cerca CF")

        lblCF = tk.Label(finestra_CercaCF, text="Inserisci dipartimento", font=("Arial", 16), fg="blue", bg="yellow")
        lblCF.grid(column=0, row=0)

        self.eDip = tk.Entry(finestra_CercaCF, width=30)
        self.eDip.grid(column=1, row=0)

        # Crea un bottone per eliminare l'utente
        btnVedi = Button(finestra_CercaCF, text="Vedi utente", command=self.cercaCF)
        btnVedi.grid(column=2, row=0)
        btnVedi.configure(pady=10, padx=5, font=('Helvetica', 13), width=5, height=1)

        btnExit = tk.Button(finestra_CercaCF, text="Exit", command=finestra_CercaCF.destroy)
        btnExit.grid(column=3, row=0)
        btnExit.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="white", bg="red")

    #                                   Fine Della Finestra Cerca Codice Fiscale

    #                                   Inizio Della Finestra Cerca Email
    def apriCercaEmail(self):
        finestra_cercaEmail = tk.Toplevel(self.root)
        finestra_cercaEmail.title("Cerca Email")

        lblAnno1 = tk.Label(finestra_cercaEmail, text="Inserisci l'anno di partenza", font=("Arial", 16), fg="blue",
                            bg="yellow")
        lblAnno1.grid(column=0, row=0)
        lblAnno2 = tk.Label(finestra_cercaEmail, text="Inserisci l'anno di fine", font=("Arial", 16), fg="blue",
                            bg="yellow")
        lblAnno2.grid(column=0, row=1)

        self.eAnno1 = tk.Entry(finestra_cercaEmail, width=30)
        self.eAnno1.grid(column=1, row=0)
        self.eAnno2 = tk.Entry(finestra_cercaEmail, width=30)
        self.eAnno2.grid(column=1, row=1)

        # Crea un bottone per eliminare l'utente
        btnVedi = Button(finestra_cercaEmail, text="Vedi email", command=self.cercaEmail)
        btnVedi.grid(column=2, row=0)
        btnVedi.configure(pady=10, padx=5, font=('Helvetica', 13), width=5, height=1)

        btnExit = tk.Button(finestra_cercaEmail, text="Exit", command=finestra_cercaEmail.destroy)
        btnExit.grid(column=2, row=1)
        btnExit.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="white", bg="red")

    #                                   Fine Della Cerca Email

    #                                   Inizio delle funzioni dei bottoni
    def inserisci(self):
        pass

    def elimina(self):
        print(self.m.elimina(self.iscritti, self.eEmail.get()))

    def cercaCF(self):
        self.m.cerca_cf(self.iscritti, self.eDip.get())

    def cercaEmail(self):
        self.m.cerca_email(self.iscritti, self.eAnno1.get(), self.eAnno2.get())

    def esci(self):
        self.root.destroy()
    #                                   Fine delle funzioni dei bottoni
