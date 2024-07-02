import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}

    def creaGrafo(self):
        self.nodi = DAO.getNodi()
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni()
        for connessione in allEdges:
            nodo1 = connessione[0]
            nodo2 =connessione[1]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes and nodo1!=nodo2:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    if connessione[2]==connessione[3]:
                        peso=2*abs(connessione[4])
                    else:
                        peso=abs(connessione[4])
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)
    def getAnalisi(self, nodo):
        lista=[]
        for vicino in self.grafo.neighbors(nodo):
            lista.append((vicino,self.grafo[nodo][vicino]["weight"]))
        return sorted(lista, key=lambda x:x[1], reverse=True)
