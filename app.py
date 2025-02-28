from tkinter import *

from view.ventana_principal import Ventana
from view.frame_consultar_art import FrameConArt
from view.frame_insert_art import FrameInsArt
from view.frame_reg_compra import FrameRegCompra

from controller.controller import Controller

from model.articulo import DBArticulos
from model.compra import DBCompra
from model.compra_articulo import DBCompraArticulo

class App(Tk):

    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('Tienda de Ropa')
        self.geometry('350x200')
        self.resizable(False, False)

        # Crear el model
        self.modelArt = DBArticulos()
        self.modelCom = DBCompra()
        self.modelComArt = DBCompraArticulo()
        self.crear_menu()

        # Crear objetos que representan la vista
        self.contenedor = Ventana(self)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center")

        self.lista_frames = {}
        self.lista_frames[0] = FrameConArt(self.contenedor)
        self.lista_frames[1] = FrameInsArt(self.contenedor)
        self.lista_frames[2] = FrameRegCompra(self.contenedor)

        self.contenedor.seleccionar_frame(self.lista_frames[0])

        #Crear el controlador
        self.controlador = Controller(self.contenedor, self.modelArt, self.modelCom, self.modelComArt)

        self.lista_frames[1].set_controlador(self.controlador)


    def crear_menu(self):
        barra_menu = Menu(self)
        self.config(menu=barra_menu)
        self.option_add('*tearOff', FALSE)

        menu_lista1 = Menu(barra_menu)
        menu_lista2 = Menu(barra_menu)

        barra_menu.add_cascade(menu=menu_lista1, label='Gestión de Artículos:')
        menu_lista1.add_command(label='Agregar Nuevo Artículo', command=self.add_art)
        menu_lista1.add_command(label='Consultar Artículos', command=self.show)

        barra_menu.add_cascade(menu=menu_lista2, label='Gestión Compras:')
        menu_lista2.add_command(label='Registrar Compra', command=self.add_com)


    def show(self):
        self.contenedor.seleccionar_frame(self.lista_frames[0])
        #TODO: sirve para leer los artículos y cargarlos
        #self.lista_frames[2].cargar_lista(self.model.leer())

    def add_art(self):
        self.contenedor.seleccionar_frame(self.lista_frames[1])

    def add_com(self):
        self.contenedor.seleccionar_frame(self.lista_frames[2])

if __name__ == "__main__":
    app = App()
    app.mainloop()
