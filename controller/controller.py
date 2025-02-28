class Controller:
    
    def __init__(self, view, modelArt, modelComp, modelCompArt):
        self.view = view
        self.modelArt = modelArt
        self.modelComp = modelComp
        self.modelCompArt = modelCompArt


    def guardar_art(self, articulo):
        self.modelArt.insert_art(articulo)
        self.view.mostrar_mensaje("El artículo se ha guardado correctamente.")

    
    def select_all(self):
        return self.modelArt.get_all_art()
    

    def select_by_name(self, nombre):
        return self.modelArt.get_art_by_name(nombre)
    
    
    def select_by_id(self, id):
        return self.modelArt.get_art_by_id(id)
    

    def update_delete(self, id):
        self.modelArt.update_delete(id)
    

    def update_delete(self, articulo):
        self.modelArt.update_art(articulo)

