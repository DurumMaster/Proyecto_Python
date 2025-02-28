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


    def insert_art(self, articulo):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            insertArt = (articulo.cod_articulo, articulo.nombre, articulo.descripcion, articulo.precio, "SI")
            print(insertArt)
            cur.execute("INSERT INTO " + NOMBRE_TABLA + " ( " + NOM_COL_COD_ART + ", " + NOM_COL_NOM + ", " + NOM_COL_DESC + ", " + NOM_COL_PRE + ", " + NOM_COL_DISP + ") VALUES (%s, %s, %s, %s, %s)", insertArt)

            con.commit()

            return True

        except Exception as e:
            print("Error al insertar articulo")
            print(e)
            return False
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()


    def get_all_art(self):
        con = None
        cur = None
        art_list = []
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " WHERE " + NOM_COL_DISP + " = 'SI'")
            
            continuar = True
            while continuar:
                reg = cur.fetchone()
                if reg == None:
                    continuar = False
                else:
                    art_list.append(Articulo(reg[0], reg[1], reg[2], reg[3], reg[4]))


        except Exception as e:
            print("Error al consultar los articulos")
            print(e)
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

        return art_list

    def get_art_by_id(self, id):
        con = None
        cur = None
        art_list = []
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " WHERE " + NOM_COL_COD_ART + " LIKE %s AND " + NOM_COL_DISP + " = 'SI'", (id + "%",))
            
            continuar = True
            while continuar:
                reg = cur.fetchone()
                if reg == None:
                    continuar = False
                else:
                    art_list.append(Articulo(reg[0], reg[1], reg[2], reg[3], reg[4]))


        except Exception as e:
            print("Error al consultar articulos por id")
            print(e)
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

        return art_list
    

    def get_art_by_name(self, nombre):
        con = None
        cur = None
        art_list = []
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " WHERE " + NOM_COL_NOM + " LIKE %s AND " + NOM_COL_DISP + " = 'SI'", (nombre + '%',))
            
            continuar = True
            while continuar:
                reg = cur.fetchone()
                if reg == None:
                    continuar = False
                else:
                    art_list.append(Articulo(reg[0], reg[1], reg[2], reg[3], reg[4]))

        except Exception as e:
            print("Error al consultar articulos por nombre")
            print(e)
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

        return art_list
    

    def select_by_id_and_name(self, id, nombre):
        con = None
        cur = None
        art_list = []
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("SELECT * FROM " + NOMBRE_TABLA + " WHERE " + NOM_COL_NOM + " LIKE %s OR " + NOM_COL_COD_ART + " LIKE %s AND " + NOM_COL_DISP + " = 'SI'", (nombre + '%', id + "%"))
            
            continuar = True
            while continuar:
                reg = cur.fetchone()
                if reg == None:
                    continuar = False
                else:
                    art_list.append(Articulo(reg[0], reg[1], reg[2], reg[3], reg[4]))

        except Exception as e:
            print("Error al consultar articulos por nombre")
            print(e)
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

        return art_list


    def update_delete(self,id):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            cur.execute("UPDATE " + NOMBRE_TABLA + " SET " + NOM_COL_DISP + " = 'NO' WHERE " + NOM_COL_COD_ART + " = %s", (id,))

            con.commit()

        except Exception as e:
            print("Error al actualizar la disponibilidad de articulos")
            print(e)
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()

    
    def update_art(self, art):
        con = None
        cur = None
        try:
            con = self.con.getConexion()
            cur = con.cursor()

            updateArt = (art.nombre, art.descripcion, art.precio, art.cod_articulo)
            cur.execute("UPDATE " + NOMBRE_TABLA + " SET " + NOM_COL_NOM + " = %s, " + NOM_COL_DESC + " = %s, " + NOM_COL_PRE + " = %s WHERE " + NOM_COL_COD_ART + " = %s", updateArt)

            con.commit()

            return True

        except Exception as e:
            print("Error al actualizar el de articulo")
            print(e)
            return False
        finally:
            if cur != None:
                cur.close()
            
            if con != None:
                con.close()