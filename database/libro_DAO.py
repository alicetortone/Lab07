from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self):
        cnx = DBConnect.get_connection()

        if cnx is not None:
            cursor = cnx.cursor()
            query = "SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca FROM libro"
            cursor.execute(query)
            result=[]
            for row in cursor:
                libro = Libro(row[0], row[1], row[2], row[3], row[4], row[5])
                result.append(libro)

            cursor.close()
            cnx.close()
            return result
        else:
            return []
