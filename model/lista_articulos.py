import configparser
import psycopg2
from model.articulo import Articulo

NOMBRE_TABLA = "ARTICULOS"
NOM_COL_COD_ART = "CODIGO_ARTICULOO"
NOM_COL_NOM = "NOMBRE"
NOM_COL_DESC = "DESCRIPCION"
NOM_COL_PRE = "PRECIO"
NOM_COL_DISP = "DISPONIBLE"

class ConDB:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("WS_Python_T1\\Pruebas\\PruebaMVC_DB\\config.ini")
        self.dbname = config['BBDD']['dbname']
        self.user = config['BBDD']['user']
        self.password = config['BBDD']['password']
        self.host = config['BBDD']['host']
        self.port = config['BBDD']['port']
        self.client_encoding= config['BBDD']['client_encoding']


    def getConexion(self):
        con = None
        try:
            con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port, client_encoding=self.client_encoding)
        
        except Exception as ex:
            print("## No se ha podido establecer la conexión##")
            print(type(ex))
            print(ex)

        return con


class ListaArticulos:
    def __init__(self):
        self.con = ConDB()