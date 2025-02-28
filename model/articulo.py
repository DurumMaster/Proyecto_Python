from db.conexion_db import ConDB
    
NOMBRE_TABLA = "ARTICULOS"
NOM_COL_COD_ART = "CODIGO_ARTICULO"
NOM_COL_NOM = "NOMBRE"
NOM_COL_DESC = "DESCRIPCION"
NOM_COL_PRE = "PRECIO"
NOM_COL_DISP = "DISPONIBLE"

class Articulo:

    def __init__(self, cod_articulo, nombre, descripcion, precio, disponible):
        self.cod_articulo = cod_articulo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponible = disponible

class DBArticulos:
    def __init__(self):
        self.con = ConDB()


    def insertArt(self, articulo):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            insertArt = [(articulo.cod_articulo, articulo.nombre, articulo.descripcion, articulo.precio, "SI")]
            cur.execute("INSERT INTO " + NOMBRE_TABLA + " VALUES( " + NOM_COL_COD_ART + ", " + NOM_COL_NOM + ", " + NOM_COL_DESC + ", " + NOM_COL_PRE + ", " + NOM_COL_DISP + ") VALUES (?, ?, ?, ?, ?)", insertArt)

            con.commit()

        except Exception :
            print("Error al insertar articulo")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()


    def getAllArt(self):
        con = None
        cur = None
        art_list = []
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " WHERE " + NOM_COL_DISP + " = 'SI'")
            
            continuar = True
            while continuar:
                reg = cur.fetchone
                if reg == None:
                    continuar = False
                else:
                    art_list.append(Articulo())


        except Exception :
            print("Error al consultar los articulos")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()


    def getArtByID(self, id):
        con = None
        cur = None
        art_list = []
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " WHERE " + NOM_COL_COD_ART + " = '?'", id)
            
            continuar = True
            while continuar:
                reg = cur.fetchone
                if reg == None:
                    continuar = False
                else:
                    art_list.append(Articulo())


        except Exception :
            print("Error al consultar articulos por id")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

        return art_list
    

    def getArtByNombre(self, nombre):
        con = None
        cur = None
        art_list = []
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " WHERE " + NOM_COL_NOM + " = '?'", nombre)
            
            continuar = True
            while continuar:
                reg = cur.fetchone
                if reg == None:
                    continuar = False
                else:
                    art_list.append(Articulo())

        except Exception :
            print("Error al consultar articulos por nombre")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

        return art_list
    

    def updateDelete(self,id):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("UPDATE " + NOMBRE_TABLA + " SET " + NOM_COL_DISP + " = 'NO' WHERE " + NOM_COL_COD_ART + " = '?'", id)

            con.commit()

        except Exception :
            print("Error al actualizar la disponibilidad de articulos")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

    
    def updateArt(self, art):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            updateArt = [(art.nombre, art.descripcion, art.precio)]
            cur.execute("UPDATE " + NOMBRE_TABLA + " SET " + NOM_COL_DESC + " = '?', SET " + NOM_COL_NOM + " = '?', SET " + NOM_COL_PRE + " = '?' WHERE " + NOM_COL_COD_ART + " = '?'", updateArt)

            con.commit()

        except Exception :
            print("Error al actualizar el de articulo")
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()