import tkinter as tk
import random

racine = tk.Tk() # Création de la fenêtre racine
racine.title("dessin") # titre

couleur_base = "blue"
def couleur():
    global couleur_base
    couleur_base = input("couleur")

objets = []

def fct_cercle():
    global objects
    X= random.randint(0,500)
    Y= random.randint(0,500)
    objets.append(carre_noir.create_oval(X, Y, 100+X, 100+Y, fill = couleur_base))
def fct_carre():
    global objects
    N= random.randint(0,500)
    V= random.randint(0,500)
    objets.append(carre_noir.create_rectangle(N, V, 100+N, 100+V, outline = couleur_base, fill= couleur_base))
def fct_croix():
    global objects
    B= random.randint(0,500)
    D= random.randint(0,500)
    objets.append(carre_noir.create_line((B, D),(100+B, 100+D), fill= couleur_base, width=3))
    objets.append(carre_noir.create_line((B+100, D),(B, D+100), fill= couleur_base, width=3))

def fct_undo():
    repeat = 1
    if len(objets) != 0:
        if carre_noir.type(objets[-1]) == "line":
            repeat = 2
        for i in range(repeat):
            carre_noir.delete(objets[-1])
            del(objets[-1])

carre_noir = tk.Canvas(racine, bg="black", height=600, width= 600) # création widget
bouton1 = tk.Button(racine, text="couleur", font = ("helvetica", "10"), command= couleur)
bouton2 = tk.Button(racine, text="cercle", font = ("helvetica", "10"), command = fct_cercle)
bouton3 = tk.Button(racine, text="carre", font = ("helvetica", "10"), command = fct_carre)
bouton4 = tk.Button(racine, text="croix", font = ("helvetica", "10"), command = fct_croix)
bouton_undo = tk.Button(racine, text="undo", bg= "grey100",fg= "blue",padx=20,font = ("helvetica", "10"),command = fct_undo)



bouton1.grid(column=1, row=0) # position widget
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)
bouton_undo.grid(column=2, row=0)
carre_noir.grid(column=1, row=1, rowspan=3)


racine.mainloop() # Lancement de la boucle principale