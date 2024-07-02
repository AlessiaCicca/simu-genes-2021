import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        grafo = self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for nodo in grafo:
            self._view.dd_gene.options.append(ft.dropdown.Option(
                               text=nodo))
        self._view.update_page()
    def handle_adiacenti(self,e):
      gene=self._view.dd_gene.value
      if gene is None:
          self._view.create_alert("Selezionare un gene")
          pass
      analisi=self._model.getAnalisi(gene)
      self._view.txt_result.controls.append(ft.Text(f"GENI ADIACENTI A {gene}"))
      for nodo, peso in analisi:
        self._view.txt_result.controls.append(ft.Text(f"{nodo} e {peso}"))
      self._view.update_page()