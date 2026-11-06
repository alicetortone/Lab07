import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = "Nessun filtro"
        self.genere_selezionato = "Nessun filtro"

    # CALLBACKS DROPDOWN
    def handle_biblioteca(self,e):
        self.biblioteca_selezionata = e.control.value

    def handle_genere_selezionato(self,e):
        self.genere_selezionato = e.control.value

    def load_data(self):
        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()

        self._view.set_biblioteche(biblioteche)
        self._view.set_generi(generi)

    def handle_mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if len(libri) == 0:
            self._view.show_alert("Nessun libro trovato!")
        else:
            self._view.mostra_libri(libri)