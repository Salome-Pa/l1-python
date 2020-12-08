r = 0
g = 0
b = 0
r = int(input("valeur de r : "))
g = int(input("valeur de g : "))
b = int(input("valeur de b : "))

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

i = int(input("coordos i"))
j = int(input("coordos j"))

def draw_pixel(i, j, color):
    """pixel (i,j) color"""
    carre_noir.create_rectangle(i,j,i - 1,j - 1, outline=color)

import random

def ecran_aleatoire():
    for i in range(256):
        for u in range(256):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            draw_pixel(i, u, get_color(r, g, b))

def degrade_gris():
    r = 0
    g = 0
    b = 0
    for i in range(256):
        for u in range(256):
            r += 1
            g += 1
            b += 1
            draw_pixel(i, u, get_color(r, g, b))

def degrade_2D():
    r = 255
    g = 0
    b = 0
    for i in range(256):
        for u in range(256):
            r -= 1
            b += 1
            g = 0
            draw_pixel(i, u, get_color(r, g, b))



import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
racine.title("dessin") # titre

carre_noir = tk.Canvas(racine, bg= "black", height=256, width= 256) # création widget
draw_pixel(i, j, get_color(r, g, b))
bouton2 = tk.Button(racine, text="aleatoire", font = ("helvetica", "10"), command = ecran_aleatoire)
bouton3 = tk.Button(racine, text="degrade gris", font = ("helvetica", "10"),command = degrade_gris )
bouton4 = tk.Button(racine, text="degrade 2D", font = ("helvetica", "10"), command = degrade_2D)


bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)
carre_noir.grid(column=1, row=1, rowspan=3)

racine.mainloop() # Lancement de la boucle principale