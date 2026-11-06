import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:

    def __init__(self, page: ft.Page):

        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):

        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(
            value="Biblioteche di Torino",
            size=38,
            weight=ft.FontWeight.BOLD
        )

        # --- Sezione 2: Filtraggio ---
        self._dd_biblioteca = ft.Dropdown(
            label="Biblioteca",
            options=[],
            on_select=self.controller.handle_biblioteca
        )

        self._dd_genere = ft.Dropdown(
            label="Genere",
            options=[],
            on_select=self.controller.handle_genere_selezionato
        )

        # --- Sezione 3: Libri ---
        self.btn_mostra = ft.Button(
            content="Mostra libri",
            on_click=self.controller.handle_mostra_libri
        )

        self.listview_libri = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=True
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(
            label="Tema scuro",
            value=True,
            on_change=self.cambia_tema
        )

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,
            self.txt_titolo,
            ft.Divider(),

            self._dd_biblioteca,
            self._dd_genere,

            self.btn_mostra,
            self.listview_libri
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """Cambia tema scuro/chiaro"""

        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.toggle_cambia_tema.value
            else ft.ThemeMode.LIGHT
        )

        self.toggle_cambia_tema.label = (
            "Tema scuro"
            if self.toggle_cambia_tema.value
            else "Tema chiaro"
        )

        self.page.update()

    def mostra_libri(self, libri):

        self.listview_libri.controls.clear()

        for libro in libri:
            self.listview_libri.controls.append(
                ft.Text(f"{libro.titolo} - {libro.autore}")
            )

        self.page.update()

    def set_biblioteche(self, biblioteche):

        self._dd_biblioteca.options = [
            ft.dropdown.Option("Nessun filtro")
        ]

        for biblioteca in biblioteche:
            self._dd_biblioteca.options.append(
                ft.dropdown.Option(biblioteca.nome)
            )

        self.page.update()

    def set_generi(self, generi):

        self._dd_genere.options = [
            ft.dropdown.Option("Nessun filtro")
        ]

        for genere in generi:
            self._dd_genere.options.append(
                ft.dropdown.Option(genere)
            )

        self.page.update()