def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    """pixel (i,j) color"""
    carre_noir.create_line(i,j,i,j, fill = color)


import tkinter as tk
import random

racine = tk.Tk() # Création de la fenêtre racine
racine.title("dessin") # titre

carre_noir = tk.Canvas(racine, bg="black", height=256, width= 256) # création widget

bouton2 = tk.Button(racine, text="aleatoire", font = ("helvetica", "10"))
bouton3 = tk.Button(racine, text="degrade gris", font = ("helvetica", "10") )
bouton4 = tk.Button(racine, text="degrade 2D", font = ("helvetica", "10") )


bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)
carre_noir.grid(column=1, row=1, rowspan=3)

racine.mainloop() # Lancement de la boucle principale