from db.conexion_db import ConDB

NOMBRE_TABLA = "COMPRA"
NOM_COL_COD_COM = "CODIGO_COMPRA"
NOM_COL_FECHA = "FECHA"
NOM_COL_PT = "PRECIO_TOTAL"

class Compra:
    def __init__(self, cod_compra, fecha, precio_total):
        self.cod_compra = cod_compra
        self.fecha = fecha
        self.precio_total = precio_total

class DBCompra:
    def __init__(self):
        self.con = ConDB()

    
    def insertComp(self, comp):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            insertCompArt = [(comp.cod_compra, comp.fecha, comp.precio_total)]
            cur.execute("INSERT INTO " + NOMBRE_TABLA + " VALUES( " + NOM_COL_COD_COM + ", " + NOM_COL_FECHA + ", " + NOM_COL_PT + ") VALUES (?, ?, ?)", insertCompArt)

            con.commit()

        except Exception :
            print("Error al insertar compra")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

