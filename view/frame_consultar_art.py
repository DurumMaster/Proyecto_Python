from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FrameConArt(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controlador = None

        self.label = ttk.Label(self, text="Consultar Artículo", font=("Arial", 14))
        self.label.pack(pady=10) 