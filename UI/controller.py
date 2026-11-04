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
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    biblioteche = self._model.get_biblioteche()
    generi = self._model.get_generi()

    # CALLBACKS DROPDOWN
    def handle_biblioteca(self,e):
        self.biblioteca_selezionata = e.control.value

    def handle_genere_selezionato(self,e):
        self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    def get_libri_selezionati(self, biblioteca, generi):
        libri = self._model.get_libri_seleizonati(self.biblioteca_selezionata, self.genere_selezionato)
