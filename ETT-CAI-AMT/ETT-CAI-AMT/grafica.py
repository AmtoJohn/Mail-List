from tkinter import Frame, Button, END
import tkinter as tk
from main import main


class Applicazione:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail List - Menu")
        self.m = main  # istanziamo il main

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
        self.btnEsci = Button(self.f1, text="Esci", command=self.apriEsci)
        self.btnEsci.grid(column=1, row=5)
        self.btnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=20, height=2, background="red",
                               foreground="white")

    #                                   Inizio Della Finestra Inserisci
    def apriInserisci(self):
        # Creazione finestra inserisci + titolo
        finestra_inserisci = tk.Toplevel(self.root)
        finestra_inserisci.title("Inserimento")

        lblGuest = tk.Label(finestra_inserisci, text="Guest", font=("Arial", 16), fg="blue", bg="yellow")
        lblGuest.grid(column=1, row=10)

        # Crea un bottone nella finestra principale
        btnGuest = Button(finestra_inserisci, text="Clicami", command=self.guest)
        btnGuest.grid(column=50, row=10)
        btnGuest.configure(pady=10, padx=5, font=('Helvetica', 15), width=10, height=2)

        lblStudenti = tk.Label(finestra_inserisci, text="Studenti", font=("Arial", 16), fg="blue", bg="yellow")
        lblStudenti.grid(column=1, row=50)

        # Crea un bottone "Clicami" nella finestra principale
        btnStudenti = Button(finestra_inserisci, text="Clicami", command=self.studenti)
        btnStudenti.grid(column=50, row=50)
        btnStudenti.configure(pady=10, padx=5, font=('Helvetica', 15), width=10, height=2)

        # teacher
        lblProfessori = tk.Label(finestra_inserisci, text="Professori", font=("Arial", 16), fg="blue", bg="yellow")
        lblProfessori.grid(column=1, row=100)

        # Crea un bottone "Clicami" nella finestra principale
        btnProfessori = Button(finestra_inserisci, text="Clicami", command=self.professori)
        btnProfessori.grid(column=50, row=100)
        btnProfessori.configure(pady=10, padx=5, font=('Helvetica', 15), width=10, height=2)

        # Crea un bottone "Clicami" nella finestra principale
        btnEsci = tk.Button(finestra_inserisci, text="Exit", command=finestra_inserisci.destroy)
        btnEsci.grid(column=50, row=150)
        btnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    # Quando clicchi il bottone viene creata la finestra Guest
    def guest(self):
        finestra_Guest = tk.Toplevel(self.root)
        finestra_Guest.title("Nuova Finestra")

        # Crea e posiziona le label e i textbox
        labels = ["Nome", "Cognome", "Anno", "Tipo", "Doc"]
        self.textboxes = []

        for i, label_text in enumerate(labels):
            lbl = tk.Label(finestra_Guest, text=label_text, font=("Arial", 16), fg="blue")
            lbl.grid(column=1, row=i * 50 + 10)

            textbox = tk.Entry(finestra_Guest, width=30)
            textbox.grid(column=50, row=i * 50 + 10)

            self.textboxes.append(textbox)

        # Crea un bottone "Exit" nella finestra
        BtnEsci = tk.Button(finestra_Guest, text="Exit", command=finestra_Guest.destroy)
        BtnEsci.grid(column=50, row=250)
        BtnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

        # Crea un pulsante "Salva" per salvare il testo dei textbox
        btnSalvaG = tk.Button(finestra_Guest, text="Salva", command=self.salvaGuest)
        btnSalvaG.grid(column=55, row=250)
        btnSalvaG.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    def salvaGuest(self):
        contenuto_caselle = []
        for textbox in self.textboxes:
            testo_inserito = textbox.get()
            contenuto_caselle.append(testo_inserito)

        # Puoi fare qualcosa con il contenuto delle caselle, ad esempio, stamparlo sulla console
        print("Contenuto delle caselle:", contenuto_caselle)

    # Creazione finestra studenti
    def studenti(self):
        finestra_studenti = tk.Toplevel(self.root)
        finestra_studenti.title("Nuova Finestra Studenti")

        # Crea e posiziona le label e i textbox per gli studenti
        labels = ["Nome", "Cognome", "Anno", "Matricola", "Corso"]
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
        labels = ["Nome", "Cognome", "Anno", "Matricola", "Corso"]
        for i, textbox in enumerate(self.textboxes_studenti):
            testo_inserito = textbox.get()
            contenuto_caselle.append(f"{labels[i]} [{testo_inserito}]")

        print("Contenuto delle caselle Studenti:")
        for item in contenuto_caselle:
            print(item)

    # Creazione finestra professori
    def professori(self):
        finestra_professori = tk.Toplevel(self.root)
        finestra_professori.title("Nuova Finestra Professori")

        # Crea e posiziona le label e i textbox per i professori
        labels = ["Nome", "Cognome", "Anno", "CodFis", "Facoltà"]
        self.textboxes_professori = []

        for i, label_text in enumerate(labels):
            lbl = tk.Label(finestra_professori, text=label_text, font=("Arial", 16), fg="blue")
            lbl.grid(column=1, row=i * 50 + 10)

            textbox = tk.Entry(finestra_professori, width=30)
            textbox.grid(column=50, row=i * 50 + 10)

            self.textboxes_professori.append(textbox)

        # Crea un bottone "Exit" nella finestra
        btnEsci = tk.Button(finestra_professori, text="Exit", command=finestra_professori.destroy)
        btnEsci.grid(column=50, row=250)
        btnEsci.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

        # Crea un pulsante "Salva" per salvare il testo dei textbox per i professori
        btnSalvaP = tk.Button(finestra_professori, text="Salva", command=self.salvaProfessori)
        btnSalvaP.grid(column=55, row=250)
        btnSalvaP.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    # Funzione per salvare il testo dei textbox per i professori
    def salvaProfessori(self):
        contenuto_caselle = []
        labels = ["Nome", "Cognome", "Anno", "Matricola", "Corso"]
        for i, textbox in enumerate(self.textboxes_studenti):
            testo_inserito = textbox.get()
            contenuto_caselle.append(f"{labels[i]} [{testo_inserito}]")

        print("Contenuto delle caselle Studenti:")
        for item in contenuto_caselle:
            print(item)

    #                                   Fine Della Finestra Inserisci

    #                                   Inizio Della Finestra Elimina
    def apriElimina(self):
        finestra_Elimina = tk.Toplevel(self.root)
        finestra_Elimina.title("Elimina")

        lblMail = tk.Label(finestra_Elimina, text="Inserisci Email", font=("Arial", 16), fg="blue", bg="yellow")
        lblMail.grid(column=1, row=10)

        eEmail = tk.Entry(finestra_Elimina, width=30)
        eEmail.grid(column=2, row=10)

        # Crea un bottone per eliminare l'utente
        btnElimina = Button(finestra_Elimina, text="Elimina", command=self.elimina)
        btnElimina.grid(column=3, row=10)
        btnElimina.configure(pady=10, padx=5, font=('Helvetica', 15), width=10, height=2)

        btnExit = tk.Button(finestra_Elimina, text="Exit", command=finestra_Elimina.destroy)
        btnExit.grid(column=5, row=20)
        btnExit.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    #                                   Fine Della Finestra Elimina

    #                                   Inizio Della Finestra Cerca Codice Fiscale
    def apriCercaCF(self):
        finestra_CercaCF = tk.Toplevel(self.root)
        finestra_CercaCF.title("Cerca CF")

        lblCF = tk.Label(finestra_CercaCF, text="Inserisci dipartimento", font=("Arial", 16), fg="blue", bg="yellow")
        lblCF.grid(column=1, row=10)

        eDip = tk.Entry(finestra_CercaCF, width=30)
        eDip.grid(column=2, row=10)

        # Crea un bottone per eliminare l'utente
        btnVedi = Button(finestra_CercaCF, text="Vedi utente", command=self.cercaCF)
        btnVedi.grid(column=2, row=10)
        btnVedi.configure(pady=10, padx=5, font=('Helvetica', 15), width=10, height=2)

        btnExit = tk.Button(finestra_CercaCF, text="Exit", command=finestra_CercaCF.destroy)
        btnExit.grid(column=5, row=20)
        btnExit.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    #                                   Fine Della Finestra Cerca Codice Fiscale

    #                                   Inizio Della Finestra Cerca Email
    def apriCercaEmail(self):
        nuova_finestra = tk.Toplevel(self.root)
        nuova_finestra.title("Cerca Email")

        lblAnno1 = tk.Label(nuova_finestra, text="Inserisci l'anno di partenza", font=("Arial", 16), fg="blue",
                            bg="yellow")
        lblAnno1.grid(column=1, row=1)
        lblAnno2 = tk.Label(nuova_finestra, text="Inserisci l'anno di partenza", font=("Arial", 16), fg="blue",
                            bg="yellow")
        lblAnno2.grid(column=1, row=2)

        eAnno1 = tk.Entry(nuova_finestra, width=30)
        eAnno1.grid(column=2, row=1)
        eAnno2 = tk.Entry(nuova_finestra, width=30)
        eAnno2.grid(column=2, row=2)

        # Crea un bottone per eliminare l'utente
        btnVedi = Button(nuova_finestra, text="Vedi email", command=self.cercaEmail)
        btnVedi.grid(column=2, row=10)
        btnVedi.configure(pady=10, padx=5, font=('Helvetica', 15), width=10, height=2)

        btnExit = tk.Button(nuova_finestra, text="Exit", command=nuova_finestra.destroy)
        btnExit.grid(column=5, row=20)
        btnExit.configure(pady=10, padx=5, font=('Helvetica', 15), width=5, height=1, fg="red")

    #                                   Fine Della Cerca Email

    #                                   Inizia Della Finestra Esci
    def apriEsci(self):
        self.root.destroy()

    #                                   Fine Della Finestra Esci

    #                                   Inizio delle funzioni dei bottoni
    def inserisci(self):
        pass

    def elimina(self):
        pass

    def cercaCF(self):
        pass

    def cercaEmail(self):
        pass

    def esci(self):
        pass
    #                                   Fine delle funzioni dei bottoni
