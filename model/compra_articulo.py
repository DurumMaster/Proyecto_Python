from db.conexion_db import ConDB

NOMBRE_TABLA = "COMPRA_ARTICULO"
NOM_COL_COD_COMP = "CODIGO_COMPRA"
NOM_COL_COD_ART = "CODIGO_ARTICULO"
NOM_COL_CANT = "CANTIDAD"

class CompraArticulo:
    def __init__(self, cod_compra, cod_articulo, cantidad):
        self.cod_compra = cod_compra
        self.cod_articulo = cod_articulo
        self.cantidad = cantidad

class DBCompraArticulo:
    def __init__(self):
        self.con = ConDB()

    def insert_comp_art(self, compraArt):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            insertCompArt = [(compraArt.cod_compra, compraArt.cod_articulo, compraArt.cantidad)]
            cur.execute("INSERT INTO " + NOMBRE_TABLA + " VALUES( " + NOM_COL_COD_COMP + ", " + NOM_COL_COD_ART + ", " + NOM_COL_CANT + ") VALUES (?, ?, ?)", insertCompArt)

            con.commit()

        except Exception :
            print("Error al insertar compra-articulo")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()