from Pila import Pila
import tkinter as tk
from tkinter import *
from random import *


class IGrafica(object):
    tamaño = 10
    x0 = 120
    y0 = 200
    x1 = 220
    y1 = 220
    pila = None
    figuras = None

    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root)
        # Declaracion de pilas
        self.pila = Pila(self.tamaño)

        self.canvas = tk.Canvas(
            root, width=300, height=220, background="white")
        self.canvas.grid(row=0, column=1, sticky="n")

        frame = Frame(self.root)
        frame.grid(row=0, column=0, sticky="n")

        texto = Label(frame, text="Programa PILA").grid(
            row=0, column=2, sticky=W + E, ipadx=50, columnspan=3)
        boton1 = Button(frame, text="PUSH", command=self.push_command).grid(
            row=1, column=2, sticky=W + E, padx=50, columnspan=3, pady=20)
        boton1 = Button(frame, text="POP",  command=self.pop_command).grid(
            row=2, column=2, sticky=W + E, padx=50, columnspan=3, pady=20)

    def push_command(self):
        if self.pila.llena():
            return
        else:
            rand1 = randint(10, 99)
            rand2 = randint(10, 99)
            self.pila.push(self.canvas.create_rectangle(
                self.x0, self.y0, self.x1, self.y1,
                fill="#aa" + str(rand1) + str(rand2)))
            self.y0 -= 20
            self.y1 -= 20

    def pop_command(self):
        if self.pila.vacia():
            return
        else:
            figura = self.pila.pop()
            self.canvas.delete(figura)
            self.y0 += 20
            self.y1 += 20


if __name__ == '__main__':
    root = tk.Tk()
    interfaz = IGrafica(root)
    root.mainloop()
