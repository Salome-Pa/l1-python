import tkinter as tk
import random

racine = tk.Tk() # Création de la fenêtre racine
racine.title("dessin") # titre


def fct_cercle():
    X= random.randint(0,500)
    Y= random.randint(0,500)
    carre_noir.create_oval(X, Y, 100+X, 100+Y, outline = "blue")
def fct_carre():
    N= random.randint(0,500)
    V= random.randint(0,500)
    carre_noir.create_rectangle(N, V, 100+N, 100+V, outline = "red", fill="red")
def fct_croix():
    B= random.randint(0,500)
    D= random.randint(0,500)
    carre_noir.create_rectangle(B, D, 100+B, 100+D, outline = "black")
    carre_noir.create_line((B, D),(100+B, 100+D), fill= "yellow", width=3)
    carre_noir.create_line((B+100, D),(B, D+100), fill= "yellow", width=3)

carre_noir = tk.Canvas(racine, bg="black", height=600, width= 600) # création widget
bouton1 = tk.Button(racine, text="couleur", font = ("helvetica", "10") )
bouton2 = tk.Button(racine, text="cercle", font = ("helvetica", "10"), command = fct_cercle)
bouton3 = tk.Button(racine, text="carre", font = ("helvetica", "10"), command = fct_carre)
bouton4 = tk.Button(racine, text="croix", font = ("helvetica", "10"), command = fct_croix)


bouton1.grid(column=1, row=0) # position widget
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)
carre_noir.grid(column=1, row=1, rowspan=3)


racine.mainloop() # Lancement de la boucle principale