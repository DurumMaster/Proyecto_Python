import psycopg2
import configparser
from model import clase_producto

NOMBRE_TABLA = "LISTA_COMPRA"
NOM_COL_NOM_PROD = "NOM_PRODUCTO"
NOM_COL_CANT = "CANTIDAD"

class ConDB:

    def __init__(self):
        """
        self.dbname = "PRUEBA_DB"
        self.user = "postgres"
        self.password = "Doctor2palancas"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.client_encoding="utf-8"
        """
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

class ListaCompra:
    
    def __init__(self):
        self.con_db = ConDB()

    def crear_tabla(self):
        con = None
        cur = None

        try:
            con = self.con_db.getConexion()

            cur = con.cursor()

            cur.execute("DROP TABLE IF EXISTS " + NOMBRE_TABLA)

            cur.execute("CREATE TABLE " + NOMBRE_TABLA + " ( ID integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 CACHE 4 ), " + NOM_COL_NOM_PROD + " text NOT NULL, " + NOM_COL_CANT + " text )")
        except Exception as ex:
            print("### No se ha podido establecer la conexión ###")
            print(type(ex))
            print(ex)
        finally:
            if cur != None:
                cur.close()
            if con != None:
                con.close()

    def insertar_producto(self, producto):
        con = None
        cur = None

        try:
            con = self.con_db.getConexion()

            cur = con.cursor()

            lista_valores = [(producto.descripcion, producto.cantidad)]
            cur.execute("INSERT INTO " + NOMBRE_TABLA + " ( " + NOM_COL_NOM_PROD + ", " + NOM_COL_CANT + ") VALUES (?,?)", lista_valores)
        
        except Exception as ex:
            print("### No se ha podido establecer la conexión ###")
            print(type(ex))
            print(ex)
        finally:
            if cur != None:
                cur.close()
            if con != None:
                con.close()

    def consultar_productos(self):
        con = None
        cur = None
        lista_productos = []

        try:
            con = ConDB.getConexion()

            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA)

            continuar = True
            while continuar:
                reg = cur.fetchone()
                if reg == None:
                    continuar = False
                else:
                    lista_productos.append(clase_producto.Producto(reg[1], reg[2]))
        
        except Exception as ex:
            print("### No se ha podido establecer la conexión ###")
            print(type(ex))
            print(ex)
        finally:
            if cur != None:
                cur.close()
            if con != None:
                con.close()

        return lista_productos

