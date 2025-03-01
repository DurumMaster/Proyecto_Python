from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

from model.articulo import Articulo

CARAC_COD = 8
MAX_CARAC_NOMBRE = 50
MAX_CARAC_DESC = 200

class FrameInsArt(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controlador = None
        
        self.label_titulo = ttk.Label(self, text="INSERTAR ARTÍCULO", font=("Arial", 12, "bold"))
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=5, sticky=W)
        
        self.label_codigo = ttk.Label(self, text="Código:")
        self.label_codigo.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.entry_codigo = ttk.Entry(self, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=5, pady=2, sticky=W)
        
        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.entry_nombre = ttk.Entry(self, width=30)
        self.entry_nombre.grid(row=2, column=1, padx=5, pady=2, sticky=W)
        
        self.label_descripcion = ttk.Label(self, text="Descripción:")
        self.label_descripcion.grid(row=3, column=0, sticky=W, padx=5, pady=2)
        self.text_descripcion = Text(self, width=30, height=5)
        self.text_descripcion.grid(row=3, column=1, padx=5, pady=2, sticky=W)
        
        self.label_precio = ttk.Label(self, text="Precio:")
        self.label_precio.grid(row=4, column=0, sticky=W, padx=5, pady=2)
        self.entry_precio = ttk.Entry(self, width=10)
        self.entry_precio.grid(row=4, column=1, padx=5, pady=2, sticky=W)

        self.frame_botones = ttk.Frame(self)
        self.frame_botones.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.btn_guardar = ttk.Button(self.frame_botones, text="GUARDAR", command=self.guardar_art)
        self.btn_guardar.grid(row=0, column=0, padx=5)
        
        self.btn_cancelar = ttk.Button(self.frame_botones, text="CANCELAR", command=self.cancelar)
        self.btn_cancelar.grid(row=0, column=1, padx=5)
        
    def set_controlador(self, controlador):
        self.controlador = controlador

    def guardar_art(self):
        codigo = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        descripcion = self.text_descripcion.get("1.0", END).strip()
        precio = self.entry_precio.get().strip()

        lista = self.controlador.select_all_insert()
        encontrado = False

        if lista:
            for i in lista:
                if i.cod_articulo == codigo:
                    encontrado = True

        if not encontrado:
            if len(codigo) != CARAC_COD or " " in codigo or not codigo:
                messagebox.showerror("Error", "El código deben ser 8 letras o números.")
                return
            if not nombre:
                messagebox.showerror("Error", "Debes introducir un nombre al artículo.")
                return
            if len(nombre) > MAX_CARAC_NOMBRE:
                messagebox.showerror("Error", "El nombre no puede tener más de 50 letras.")
                return
            if not descripcion:
                messagebox.showerror("Error", "Debes introducir una descripción al artículo.")
                return
            if len(descripcion) > MAX_CARAC_DESC:
                messagebox.showerror("Error", "La descripción no puede tener más de 200 letras.")
                return
            precio = precio.replace(',', '.')
            precio_pattern = r"^\d+(\.\d{1,2})?$"
            if not re.match(precio_pattern, precio):
                messagebox.showerror("Error", "El precio debe ser un número positivo con hasta 2 decimales.")
                return
            
            articulo = Articulo(codigo, nombre, descripcion, precio, "SI")

            if self.controlador:
                self.controlador.guardar_art(articulo)
                self.limpiar_datos()
                self.entry_codigo.focus()
        else:
            messagebox.showerror("Error","El código introducido ya está registrado")

    def cancelar(self):
        respuesta = messagebox.askquestion("Confirmar cancelación", "¿Estás seguro de que deseas cancelar y limpiar los datos?")
    
        if respuesta == 'yes':
            self.limpiar_datos()

    def limpiar_datos(self):
        self.entry_codigo.delete(0,"end")
        self.entry_nombre.delete(0,"end")
        self.text_descripcion.delete("1.0",END)
        self.entry_precio.delete(0,"end")
            

