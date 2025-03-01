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

    
    def insert_comp(self, comp):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            insertCompArt = (comp.fecha, comp.precio_total)
            cur.execute("INSERT INTO " + NOMBRE_TABLA + " ( " + NOM_COL_FECHA + ", " + NOM_COL_PT + ") VALUES (%s, %s)", insertCompArt)

            con.commit()

            if cur.rowcount:
                return True
            else:
                return False

        except Exception as e:
            print("Error al insertar compra")
            print(e)
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()


    def get_ultimo_id(self):
        con = None
        cur = None
        id = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " ORDER BY " + NOM_COL_COD_COM + " DESC")

            id = cur.fetchone()

            con.commit()

        except Exception as e:
            print("Error al insertar compra")
            print(e)
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()
        return id