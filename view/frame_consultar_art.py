from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class FrameConArt(ttk.Frame):
    def __init__(self, parent, lista=[]):
        super().__init__(parent, style="Card.TFrame")
        self.lista = lista
        self.controlador = None

        self.label_titulo = ttk.Label(self, text="")
        self.label_titulo.grid(row=0, column=0, columnspan=2)

        self.label_titulo = ttk.Label(self, text="CONSULTA DE ARTÍCULOS", font=("Arial", 14, "bold"), foreground="#2C3E50")
        self.label_titulo.grid(row=1, column=0, columnspan=2, pady=10)

        self.frame_formulario = ttk.Frame(self, padding=10, style="InnerCard.TFrame")
        self.frame_formulario.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky=EW)
        
        self.label_codigo = ttk.Label(self.frame_formulario, text="Código:")
        self.label_codigo.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.entry_codigo = ttk.Entry(self.frame_formulario, width=50)
        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.label_nombre = ttk.Label(self.frame_formulario, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(self.frame_formulario, width=50)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.btn_buscar = ttk.Button(self, text="🔍 BUSCAR", command=self.select, style="Accent.TButton")
        self.btn_buscar.grid(row=3, column=0, columnspan=2, pady=10)

        self.frame_tabla = ttk.Frame(self, padding=10, style="InnerCard.TFrame")
        self.frame_tabla.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=NSEW)
        
        self.scroll_y = ttk.Scrollbar(self.frame_tabla, orient=VERTICAL)
        self.tree = ttk.Treeview(
            self.frame_tabla,
            columns=("Código", "Nombre"),
            selectmode="browse",
            show="headings",
            height=7,
            yscrollcommand=self.scroll_y.set
        )
        self.scroll_y.config(command=self.tree.yview)

        self.tree.column("Código", width=120, anchor=CENTER)
        self.tree.column("Nombre", width=250, anchor=W)
        self.tree.heading("Código", text="CÓDIGO")
        self.tree.heading("Nombre", text="NOMBRE")

        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll_y.pack(side=RIGHT, fill=Y)


        self.frame_botones = ttk.Frame(self)
        self.frame_botones.grid(row=5, column=0, columnspan=2, pady=15)
        
        self.btn_modificar = ttk.Button(self.frame_botones, text="✏️ MODIFICAR", command=self.modify, style="Modify.TButton")
        self.btn_modificar.grid(row=0, column=0, padx=10)
        
        self.btn_eliminar = ttk.Button(self.frame_botones, text="🗑️ ELIMINAR", command=self.delete, style="Danger.TButton")
        self.btn_eliminar.grid(row=0, column=1, padx=10)
        
        self.estilizar_widgets()
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def estilizar_widgets(self):
        style = ttk.Style()
        
        style.configure("TFrame", background="#ECF0F1")
        
        style.configure("Card.TFrame", background="#FFFFFF", relief="raised", borderwidth=2)
        style.configure("InnerCard.TFrame", background="#F8F9FA", relief="groove", borderwidth=1)
        
        style.configure("Accent.TButton", font=("Arial", 10, "bold"), foreground="#000000", background="#00FF00", padding=5)
        style.map("Accent.TButton", background=[("active", "#229954")])

        style.configure("Modify.TButton", font=("Arial", 10, "bold"), foreground="#000000", background="#FFA500", padding=5)
        style.map("Modify.TButton", background=[("active", "#229954")])
        
        style.configure("Danger.TButton", font=("Arial", 10, "bold"), foreground="#000000", background="#FF0000", padding=5)
        style.map("Danger.TButton", background=[("active", "#229954")])

    
    def modify(self):

        item = self.tree.selection()
        if not item:
            messagebox.showerror("Error", "Por favor, selecciona un artículo para modificar.")
            return

        datos = self.tree.item(item, "values")
        codigo = datos[0] 

        self.controlador.show_modify(codigo)


    def delete(self):
        articulo = self.tree.selection()
        if len(articulo) == 0:
            messagebox.askokcancel("Error", "No has seleccionado ningún artículo")
        else:
            respuesta = messagebox.askquestion("Eliminar artículo", "¿Estás seguro de que quieres eliminar el producto?")
            if respuesta == "yes":
                item = self.tree.item(articulo[0])
                print(item['values'][0])
                self.controlador.update_delete(str(item['values'][0]))
                self.tree.delete(articulo[0])


    def select(self):
        codigo = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        lista_art = []
        if len(codigo) == 0:
            if len(nombre) == 0:
                lista_art = self.controlador.select_all()
            else:
                lista_art = self.controlador.select_by_name(nombre)
        elif len(codigo) != 0 and len(nombre) != 0:
            lista_art = self.controlador.select_by_id_and_name(codigo, nombre)
        else:
            lista_art = self.controlador.select_by_id(codigo)

        self.insertar_en_tabla(lista_art)


    def limpiar_tabla(self):
        articulos = self.tree.get_children()
        for i in articulos:
            self.tree.delete(i)

    
    def insertar_en_tabla(self, lista=[]):
        self.limpiar_tabla()
        if lista:
            for i in lista:
                self.tree.insert("", "end", values=(i.cod_articulo, i.nombre))
        else:
            messagebox.showerror("Error", "No se ha encontrado ningún artículo.")


    def set_controlador(self, controlador):
        self.controlador = controlador

