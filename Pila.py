from tkinter import messagebox


class Pila(object):
    tamaño = None
    tope = None
    datos = None

    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.datos = []

    def push(self, dato):
        if self.llena():
            return False
        else:
            self.datos.append(dato)
            return True

    def pop(self):
        if self.vacia():
            return True
        else:
            valor = self.datos.pop()
            return valor

    def llena(self):
        if (len(self.datos) == self.tamaño):
            messagebox.showinfo("Estado de la Pila", "Pila llena")
            return True
        else:
            return False

    def vacia(self):
        if len(self.datos) == 0:
            messagebox.showinfo("Estado de la Pila", "Pila Vacia")
            return True
        else:
            return False

    def mostar(self):
        cad = ""
        for v in self.datos:
            cad = cad + str(v) + " "
        messagebox.showinfo("Estado de la Pila", cad)
