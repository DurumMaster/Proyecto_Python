import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FrameRegCompra(tk.Frame):
     def __init__(self, parent):
          super().__init__(parent)
          self.grid(sticky=tk.NSEW)
          self.create_widgets()

     def create_widgets(self):
          # Título
          self.label_titulo = ttk.Label(self, text="REGISTRAR COMPRA", font=("Arial", 12, "bold"))
          self.label_titulo.grid(row=0, column=0, columnspan=3, pady=5, sticky=tk.W)

          # Nombre
          self.label_nombre = ttk.Label(self, text="Nombre:")
          self.label_nombre.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
          self.entry_nombre = ttk.Entry(self, width=30)
          self.entry_nombre.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W)
          self.btn_buscar = ttk.Button(self, text="BUSCAR", command=self.buscar)
          self.btn_buscar.grid(row=1, column=2, padx=5, pady=2)

          # Tabla de códigos y nombres
          self.frame_tabla = ttk.Frame(self)
          self.frame_tabla.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W+tk.E)

          self.scrollbar_x = ttk.Scrollbar(self.frame_tabla, orient=tk.HORIZONTAL)
          self.scrollbar_y = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL)

          self.treeview = ttk.Treeview(self.frame_tabla, columns=("codigo", "nombre"), xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)
          self.treeview.heading("#0", text="")
          self.treeview.heading("codigo", text="CODIGO")
          self.treeview.heading("nombre", text="NOMBRE")
          self.treeview.column("#0", width=0, stretch=tk.NO)
          self.treeview.column("codigo", anchor=tk.W, width=100)
          self.treeview.column("nombre", anchor=tk.W, width=200)

          self.scrollbar_x.config(command=self.treeview.xview)
          self.scrollbar_y.config(command=self.treeview.yview)

          self.treeview.grid(row=0, column=0, sticky=tk.NSEW)
          self.scrollbar_x.grid(row=1, column=0, sticky=tk.EW)
          self.scrollbar_y.grid(row=0, column=1, sticky=tk.NS)

          # Cantidad
          self.label_cantidad = ttk.Label(self, text="Cantidad:")
          self.label_cantidad.grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
          self.spin_cantidad = ttk.Spinbox(self, from_=1, to=5, width=5)
          self.spin_cantidad.grid(row=3, column=1, padx=5, pady=2, sticky=tk.W)
          self.btn_anadir = ttk.Button(self, text="AÑADIR", command=self.add)
          self.btn_anadir.grid(row=3, column=2, padx=5, pady=2)

          # Lista con scrollbar
          self.frame_lista = ttk.Frame(self)
          self.frame_lista.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W+tk.E)

          self.scrollbar_lista = ttk.Scrollbar(self.frame_lista, orient=tk.VERTICAL)
          self.listbox = tk.Listbox(self.frame_lista, height=10, width=50, yscrollcommand=self.scrollbar_lista.set)
          self.scrollbar_lista.config(command=self.listbox.yview)

          self.listbox.grid(row=0, column=0, sticky=tk.NSEW)
          self.scrollbar_lista.grid(row=0, column=1, sticky=tk.NS)

          # Precio total
          self.label_precio_total = ttk.Label(self, text="Precio total:")
          self.label_precio_total.grid(row=5, column=0, sticky=tk.W, padx=5, pady=2)
          self.entry_precio_total = ttk.Entry(self, width=20)
          self.entry_precio_total.grid(row=5, column=1, padx=5, pady=2, sticky=tk.W)

          # Botón registrar
          self.btn_registrar = ttk.Button(self, text="REGISTRAR")
          self.btn_registrar.grid(row=6, column=0, columnspan=3, pady=10)

          # Ajuste de columnas
          self.columnconfigure(0, weight=1)
          self.columnconfigure(1, weight=1)
          self.columnconfigure(2, weight=1)

     def add(self):
          selected_item = self.treeview.selection()
          if not selected_item:
               messagebox.showerror("Error", "Debe seleccionar un artículo antes de añadirlo.")
               return

          item_values = self.treeview.item(selected_item, "values")
          codigo = item_values[0]
          nombre = item_values[1]
          descripcion = item_values[2]
          cantidad = self.spin_cantidad.get() 
          precio = item_values[3]

          item_text = f"""
- Código: {codigo}
{nombre}
Descripción: {descripcion}
Cantidad: {cantidad}
Precio unidad: {precio}€
"""

          self.listbox.insert("end", item_text)

     def buscar(self):
          nombre = self.entry_nombre.get().strip()
          lista_art = []
          if len(nombre) == 0:
               messagebox("Error", "Debe introducir un nombre en el filtro para poder buscar.")
          else:
               lista_art = self.controlador.select_by_name(nombre)

          self.insertar_en_tabla(lista_art)


     def insertar_en_tabla(self, lista=[]):
          self.limpiar_tabla()
          if lista:
               for i in lista:
                    self.tree.insert("", "end", values=(i.cod_articulo, i.nombre))
          else:
               messagebox("Error", "No se ha encontrado ningún artículo.")


     def limpiar_tabla(self):
          articulos = self.tree.get_children()
          for i in articulos:
               self.tree.delete(i)
       

     def set_controlador(self, controlador):
      self.controlador = controlador