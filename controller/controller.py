from view.frame_mod_art import FrameModArt

class Controller:
    
    def __init__(self, view, modelArt, modelComp, modelCompArt):
        self.view = view
        self.modelArt = modelArt
        self.modelComp = modelComp
        self.modelCompArt = modelCompArt

    
    def select_all(self):
        return self.modelArt.get_all_art()
    

    def select_by_name(self, nombre):
        return self.modelArt.get_art_by_name(nombre)
    
    
    def select_by_id(self, id=""):
        return self.modelArt.get_art_by_id(id)
    
    
    def select_by_id_and_name(self, id="", name=""):
        return self.modelArt.select_by_id_and_name(id, name)
    

    def update_delete(self, id):
        self.modelArt.update_delete(id)
    

    def update_art(self, articulo):
        isModificado = self.modelArt.update_art(articulo)
        if isModificado:
            self.view.mostrar_mensaje("El artículo se ha modificado correctamente.")
        else:
            self.view.mensaje_error("Ha ocurrido un error al modificar el artículo.")
        self.show_consultar()


    def guardar_art(self, articulo):
        isInsertado = self.modelArt.insert_art(articulo)
        if isInsertado:
            self.view.mostrar_mensaje("El artículo se ha guardado correctamente.")
        else:
            self.view.mensaje_error("Ha ocurrido un error al guardar el artículo.")


    def show_modify(self, codigo):
        articulos = self.modelArt.get_art_by_id(codigo)
        if articulos:
            art = articulos[0]
            mod_frame = self.view.frames[3]
            mod_frame.cargar_datos(art)
            self.view.seleccionar_frame(mod_frame)
        else:
            self.view.mostrar_mensaje("No se encontró el artículo")


    def show_consultar(self):
        con_frame = self.view.frames[0]
        self.view.seleccionar_frame(con_frame)
        lista = self.select_all()
        con_frame.insertar_en_tabla(lista)
        