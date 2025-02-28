from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Ventana(ttk.Frame):


    def __init__(self, parent):
        super().__init__(parent)
        self.frame = None
        self.frames = []


    def seleccionar_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()    


    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Info", mensaje)


    def mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)