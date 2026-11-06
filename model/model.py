from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        libri=self._libro_dao.get_libri()
        biblioteche = self._biblioteca_dao.get_biblioteche()

        for libro in libri:
            for b in biblioteche:
                if libro.id_biblioteca == b.id:
                    libro.biblioteca = b
                #faccio questo per associae ogni libro alla sua biblioteca

        if biblioteca != "Nessun filtro" :
            libri_filtrati  = []
            for libro in libri:
                if libro.biblioteca.nome == biblioteca :
                    libri_filtrati.append(libro)
            libri = libri_filtrati

        if genere != "Nessun filtro":
            libri_filtrati = []
            for libro in libri:
                if libro.genere == genere:
                    libri_filtrati.append(libro)
            libri = libri_filtrati

        return libri

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        libri = self._libro_dao.get_libri()
        generi = []
        for libro in libri:
            if libro.genere not in generi:
                generi.append(libro.genere)

        return generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_biblioteche()
