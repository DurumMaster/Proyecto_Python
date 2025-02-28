from tkinter import *
from tkinter import ttk

class FrameConArt(ttk.Frame):
    def __init__(self, parent, lista=[]):
        super().__init__(parent)
        self.lista = lista
        self.controlador = None

        # Título
        self.label_titulo = ttk.Label(self, text="BÚSQUEDA DE ARTÍCULOS", font=("Arial", 12, "bold"))
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

        # Botón de búsqueda
        self.btn_buscar = ttk.Button(self, text="BUSCAR")
        self.btn_buscar.grid(row=3, column=1, pady=5, sticky=E)

        # Frame para la tabla y scrollbar
        self.frame_tabla = ttk.Frame(self)
        self.frame_tabla.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Scrollbar vertical
        self.scroll_y = ttk.Scrollbar(self.frame_tabla, orient=VERTICAL)
        
        # Tabla (Treeview)
        self.tree = ttk.Treeview(
            self.frame_tabla, 
            columns=("Código", "Nombre"), 
            show="headings", 
            height=5, 
            yscrollcommand=self.scroll_y.set
        )
        self.scroll_y.config(command=self.tree.yview)
        
        self.tree.column("Código", width=100, anchor=CENTER)
        self.tree.column("Nombre", width=200, anchor=W)
        self.tree.heading("Código", text="CÓDIGO")
        self.tree.heading("Nombre", text="NOMBRE")

        # Empaquetar elementos dentro del frame de la tabla
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # Botones de modificar y eliminar
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_modificar = ttk.Button(self.frame_botones, text="MODIFICAR")
        self.btn_modificar.grid(row=0, column=0, padx=5)

        self.btn_eliminar = ttk.Button(self.frame_botones, text="ELIMINAR")
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        # Ajustar tamaño de columnas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def set_controlador(self, controlador):
        self.controlador = controlador

