from tkinter import Label, Button, Toplevel, Tk
from grafica import Applicazione


def app(root):
    root_b = Toplevel(root)
    root_b.title("Mail List")
    root_b.configure(bg='darkgray')
    a = Applicazione(root_b)
    return a



def main():
    root = Tk()
    root.geometry("200x100")
    root.title("Lobby ")
    lbl_bv = Label(text="Benvenuto nel progetto di Ett-Amt-Cai")
    lbl_bv.grid(column=0, row=0)
    b1 = Button(root, text='Avvia', command=lambda: app(root))
    b1.grid(column=0, row=2)
    root.mainloop()


main()
