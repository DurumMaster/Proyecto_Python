from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

from model.articulo import Articulo

MAX_CARAC_NOMBRE = 50
MAX_CARAC_DESC = 200

class FrameModArt(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controlador = None

        self.label_titulo = ttk.Label(self, text="")
        self.label_titulo.grid(row=0, column=0, columnspan=2)

        self.label_titulo = ttk.Label(self, text="MODIFICAR ARTÍCULO", font=("Arial", 14, "bold"), foreground="#2C3E50")
        self.label_titulo.grid(row=1, column=0, columnspan=2, pady=10)

        self.label_codigo = ttk.Label(self, text="Código:")
        self.label_codigo.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_codigo = ttk.Entry(self, width=20, state="disabled", style="TEntry")
        self.entry_codigo.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre = ttk.Entry(self, width=30, style="TEntry")
        self.entry_nombre.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.label_descripcion = ttk.Label(self, text="Descripción:")
        self.label_descripcion.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.text_descripcion = Text(self, width=30, height=5, wrap="word", font=("Arial", 10), bd=1, relief="solid")
        self.text_descripcion.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.label_precio = ttk.Label(self, text="Precio:")
        self.label_precio.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.entry_precio = ttk.Entry(self, width=10, style="TEntry")
        self.entry_precio.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.frame_botones = ttk.Frame(self, padding=10, style="InnerCard.TFrame")
        self.frame_botones.grid(row=6, column=0, columnspan=2, pady=15)

        self.btn_guardar = ttk.Button(self.frame_botones, text="✔ GUARDAR", command=self.guardar, style="Accent.TButton")
        self.btn_guardar.grid(row=0, column=0, padx=10)

        self.btn_cancelar = ttk.Button(self.frame_botones, text="❌ CANCELAR", command=self.cancelar, style="Cancel.TButton")
        self.btn_cancelar.grid(row=0, column=1, padx=10)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.estilizar_widgets()

    def estilizar_widgets(self):
        style = ttk.Style()
        style.configure("Accent.TButton", background="#3498db", foreground="white", padding=10)
        style.configure("Cancel.TButton", background="#e74c3c", foreground="white", padding=10)
        style.configure("TEntry", padding=5)
        style.configure("InnerCard.TFrame", background="#ecf0f1")

    def set_controlador(self, controlador):
        self.controlador = controlador

    def guardar(self):

        nombre = self.entry_nombre.get().strip()
        descripcion = self.text_descripcion.get("1.0", END).strip()
        precio = self.entry_precio.get().strip()

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
        
        articulo = Articulo(self.entry_codigo.get(), nombre, descripcion, precio, "SI")
        
        if articulo:
            respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres modificar este artículo?")
            if respuesta:
                self.controlador.update_art(articulo)


    def cancelar(self):
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres cancelar? Se borrarán todos los datos.")
        if respuesta:
            self.controlador.show_consultar()

    def cargar_datos(self, articulo):
        self.clean()

        self.entry_codigo.config(state="normal")
        self.entry_codigo.insert(0, articulo.cod_articulo)
        self.entry_codigo.config(state="disabled")

        self.entry_nombre.insert(0, articulo.nombre)

        self.text_descripcion.insert("1.0", articulo.descripcion)

        self.entry_precio.insert(0, articulo.precio)


    def clean(self):
        self.entry_codigo.config(state="normal")
        self.entry_codigo.delete(0, END)
        self.entry_codigo.config(state="disabled")
        
        self.entry_nombre.delete(0, END)
        self.text_descripcion.delete("1.0", END)
        self.entry_precio.delete(0, END)
