import Funcoes

arq = open('Entrada_Test.txt', 'r')
FirstLine = arq.readline().rstrip()
FirstLine = FirstLine.split()
Vertices = int(FirstLine[0])
Arestas = int(FirstLine[1])


Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]
Lista = [[] for x in range(Vertices)]

for i in range(0, Arestas):
    Aresta = arq.readline()
    Aresta = Aresta.split(" ")
    x = int(Aresta[0])
    y = int(Aresta[1])
    z = int(Aresta[2])
    Lista[x].append((y))
    Lista[y].append((x))
    Matriz[x][y] = 1
    Matriz[y][x] = 1

Funcoes.busca_Largura(Matriz, 0,1)
Funcoes.busca_Profundidade(Lista,0,2)
arq.close()