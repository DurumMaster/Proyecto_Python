class Controller:
    
    def __init__(self, view, modelArt, modelComp, modelCompArt):
        self.view = view
        self.modelArt = modelArt
        self.modelComp = modelComp
        self.modelCompArt = modelCompArt

    def guardar_art(self, articulo):
        self.modelArt.insert_art(articulo)
        self.view.mostrar_mensaje("El artículo se ha guardado correctamente.")