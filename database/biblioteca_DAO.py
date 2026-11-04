from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def select_biblioteca(self,nome_biblioteca):
        db = DBConnect()
        cnx = db.get_connection()

        if cnx is not None:
            query = f"SELECT id, nome, indirizzo  FROM biblioteca WHERE nome = %s"
            cursor = cnx.cursor()
            cursor.execute(query,(nome_biblioteca,))
            result = []
            for row in cursor:
                biblioteca = Biblioteca(row[0], row[1], row[2])
                result.append(biblioteca)

            cursor.close()
            cnx.close()
            return result
        else:
            return []