from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FrameInsArt(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controlador = None

        self.label = ttk.Label(self, text="Insertar Artículo", font=("Arial", 14))
        self.label.pack(pady=10) 

    def set_controlador(self, controlador):
        self.controlador = controlador