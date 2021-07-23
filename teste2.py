import Funcoes
arq = open('En.txt', 'r')
FirstLine = arq.readline().rstrip()
FirstLine = FirstLine.split()
Vertices = int(FirstLine[0])
Arestas = int(FirstLine[1])
print(Vertices)
Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]

for i in range(0, Arestas):
    Aresta = arq.readline()
    Aresta = Aresta.split(" ")
    x = int(Aresta[0])
    y = int(Aresta[1])
    z = int(Aresta[2])
    Matriz[x][y] = z
    Matriz[y][x] = z

