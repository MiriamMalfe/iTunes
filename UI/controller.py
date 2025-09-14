import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handleCreaGrafo(self, e):
        self._model.creaGrafo(self._view._txtInDurata.value)
        self.fillDDAlbum()

    def getSelectedAlbum(self, e):  #readDDAlbum
        if e.control.data is None:
            self.album = None
        else:
            self.album = e.control.data

    def fillDDAlbum(self):
        listaNodi = self._model.getListaNodi()
        for n in listaNodi:
            self._view._ddAlbum .options.append(ft.dropdown.Option(text=n.Title,
                                                                    data=n,
                                                                    on_click=self.getSelectedAlbum))
        self._view.update_page()

    def getSelectedAlbum(self,e):
        if e.control.data is None:
            self.album = None
        else:
            self.album = e.control.data

    def handleAnalisiComp(self, e):
        self._model.componenteConnessa(self.album)

    def handleGetSetAlbum(self, e):
        pass