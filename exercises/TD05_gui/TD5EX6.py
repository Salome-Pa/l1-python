import tkinter as tk

racine = tk.Tk()
canvas = tk.Canvas(racine, width= 500, height= 500, bg= "black")
canvas.grid()

def pixel(coord):
    canvas.create_line((coord.x, coord.y), (coord.x + 1, coord.y), fill = "red")
canvas.bind('<Button-1>', pixel)

racine.mainloop()

