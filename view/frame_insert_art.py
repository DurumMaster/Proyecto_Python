from tkinter import *
from tkinter import ttk

class FrameInsArt(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controlador = None
        
        # Título
        self.label_titulo = ttk.Label(self, text="INSERTAR ARTÍCULO", font=("Arial", 12, "bold"))
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=5, sticky=W)
        
        # Código
        self.label_codigo = ttk.Label(self, text="Código:")
        self.label_codigo.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.entry_codigo = ttk.Entry(self, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=5, pady=2, sticky=W)
        
        # Nombre
        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.entry_nombre = ttk.Entry(self, width=30)
        self.entry_nombre.grid(row=2, column=1, padx=5, pady=2, sticky=W)
        
        # Descripción
        self.label_descripcion = ttk.Label(self, text="Descripción:")
        self.label_descripcion.grid(row=3, column=0, sticky=W, padx=5, pady=2)
        self.text_descripcion = Text(self, width=30, height=5)
        self.text_descripcion.grid(row=3, column=1, padx=5, pady=2, sticky=W)
        
        # Precio
        self.label_precio = ttk.Label(self, text="Precio:")
        self.label_precio.grid(row=4, column=0, sticky=W, padx=5, pady=2)
        self.entry_precio = ttk.Entry(self, width=10)
        self.entry_precio.grid(row=4, column=1, padx=5, pady=2, sticky=W)
        
        # Botones
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.btn_guardar = ttk.Button(self.frame_botones, text="GUARDAR")
        self.btn_guardar.grid(row=0, column=0, padx=5)
        
        self.btn_cancelar = ttk.Button(self.frame_botones, text="CANCELAR")
        self.btn_cancelar.grid(row=0, column=1, padx=5)
        
    def set_controlador(self, controlador):
        self.controlador = controlador
