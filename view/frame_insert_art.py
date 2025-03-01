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
        super().__init__(parent, style="Card.TFrame")
        self.controlador = None

        self.label_titulo = ttk.Label(self, text="")
        self.label_titulo.grid(row=0, column=0, columnspan=2)

        self.label_titulo = ttk.Label(self, text="AGREGAR NUEVO ARTÍCULO", font=("Arial", 16, "bold"), foreground="#2C3E50")
        self.label_titulo.grid(row=1, column=0, columnspan=2, pady=10)

        self.frame_formulario = ttk.Frame(self, padding=10, style="InnerCard.TFrame")
        self.frame_formulario.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky=EW)

        self.label_codigo = ttk.Label(self.frame_formulario, text="Código:")
        self.label_codigo.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.entry_codigo = ttk.Entry(self.frame_formulario, width=20)
        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.label_nombre = ttk.Label(self.frame_formulario, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(self.frame_formulario, width=30)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.label_descripcion = ttk.Label(self.frame_formulario, text="Descripción:")
        self.label_descripcion.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.text_descripcion = Text(self.frame_formulario, width=30, height=5)
        self.text_descripcion.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        self.label_precio = ttk.Label(self.frame_formulario, text="Precio:")
        self.label_precio.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.entry_precio = ttk.Entry(self.frame_formulario, width=10)
        self.entry_precio.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
        # Botones
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.grid(row=3, column=0, columnspan=2, pady=15)
        
        self.btn_guardar = ttk.Button(self.frame_botones, text="✔ GUARDAR", command=self.guardar_art, style="Accent.TButton")
        self.btn_guardar.grid(row=0, column=0, padx=10)
        
        self.btn_cancelar = ttk.Button(self.frame_botones, text="❌ CANCELAR", command=self.cancelar, style="Danger.TButton")
        self.btn_cancelar.grid(row=0, column=1, padx=10)
        
        self.estilizar_widgets()

    def estilizar_widgets(self):
        style = ttk.Style()
        
        style.configure("TFrame", background="#ECF0F1")
        style.configure("Card.TFrame", background="#FFFFFF", relief="raised", borderwidth=2)
        style.configure("InnerCard.TFrame", background="#F8F9FA", relief="groove", borderwidth=1)
        
        style.configure("Accent.TButton", font=("Arial", 10, "bold"), foreground="#000000", background="#27AE60", padding=5)
        style.map("Accent.TButton", background=[("active", "#229954")])
        
        style.configure("Danger.TButton", font=("Arial", 10, "bold"), foreground="#000000", background="#E74C3C", padding=5)
        style.map("Danger.TButton", background=[("active", "#229954")])
        
    def set_controlador(self, controlador):
        self.controlador = controlador

    def guardar_art(self):
        codigo = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        descripcion = self.text_descripcion.get("1.0", END).strip()
        precio = self.entry_precio.get().strip()

        lista = self.controlador.select_all

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

    def cancelar(self):
        respuesta = messagebox.askquestion("Confirmar cancelación", "¿Estás seguro de que deseas cancelar y limpiar los datos?")
    
        if respuesta == 'yes':
            self.limpiar_datos()

    def limpiar_datos(self):
        self.entry_codigo.delete(0,"end")
        self.entry_nombre.delete(0,"end")
        self.text_descripcion.delete("1.0",END)
        self.entry_precio.delete(0,"end")
            

