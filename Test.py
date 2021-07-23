import matplotlib.pyplot as grafico
import Funcoes

arq = open('collaboration_graph.txt', 'r')
Lista = Funcoes.lista(arq)
grafico.xlabel("Vertice")
grafico.ylabel("Grau")
grafico.axis(ymin = 0, ymax = max(Funcoes.informacoes(Lista, 2)))
grafico.axis(xmin = 0, xmax = len(Lista))
grafico.plot(Funcoes.informacoes(Lista, 2))
grafico.show()
