import tkinter as tk

racine = tk.Tk()
canvas = tk.Canvas(racine, width= 500, height= 500, bg= "black")
canvas.grid()

def pixel(event):
    canvas.create_line((event.x, event.y), (event.x + 1, event.y), fill = "red")
canvas.bind('<Button-1>', pixel)

racine.mainloop()


nb_clic = 0
pt = (0,0)

def draw_line(event):
    global nb_clic, pt
    if nb_clic == 0:
        nb
