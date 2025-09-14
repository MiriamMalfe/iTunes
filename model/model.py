import networkx as nx

from UI import controller
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def aggiungiNodi(self, d):
        listaAlbum = DAO.getAllAlbum()

        listaNodi= []
        for a in listaAlbum:
            somma = 0
            for t in a.listaTracce:
                somma= somma + (t.Milliseconds)/60000
            if somma > int(d):
                listaNodi.append(a)

        if somma == 0:
            pass
        else:
            self.grafo.add_nodes_from(listaNodi)

    def aggiungiArchi(self):
        listaNodi = list(self.grafo.nodes)

        for a1 in listaNodi: #per ogni album del nodo 1
            for a2 in listaNodi: #per ogni album nodo 2
                if a1 == a2:
                    pass
                else:
                    lista1 = a1.listaTracce #creo lista tracce album1
                    lista2 = a2.listaTracce #creo lista tracce album2
                    for t1 in lista1:  #per ogni traccia nella lista1
                        for t2 in lista2: #per ogni traccia nella lista2
                            pl1 = DAO.playlistId(t1.TrackId)  # creo lista di playlist id in cui c'è traccia 1
                            pl2 = DAO.playlistId(t2.TrackId)  # creo lista di playlist id in cui c'è traccia 2
                            if pl1 == pl2:  #se le due playlist sono uguali creo arco tra i due nodi
                                self.grafo.add_edge(a1, a2)


    def creaGrafo(self, d):
        self.aggiungiNodi(d)
        print(f"il numero di nodi è: {self.grafo.number_of_nodes()}")
        self.aggiungiArchi()
        print(f"numero di archi è: {self.grafo.number_of_edges()} ")

    def getListaNodi(self):
        return list(self.grafo.nodes)

    def componenteConnessa(self, album):
        conn = nx.node_connected_component(self.grafo, album)  # mi fa direttamente la coponente connessa
        print("Lunghezza componente connessa: ", len(conn))

        durata = 0
        for a in conn:
            for t in a.listaTracce:
                durata = durata+t.Milliseconds
        print(f"Durata complessiva: {durata}")


