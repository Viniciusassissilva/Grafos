arq = open('Entrada_Test.txt', 'r')
FirstLine = arq.readline().rstrip()
FirstLine = FirstLine.split()
Aresta = int(FirstLine[0])
Vertice = int(FirstLine[1])


Matriz = [[0 for _ in range(Aresta)] for _ in range(Aresta)]
Lista = [[] for x in range(Aresta)]

for i in range(0, Vertice):
    Vertices = arq.readline()
    Vertices = Vertices.split(" ")
    x = int(Vertices[0])
    y = int(Vertices[1])
    z = int(Vertices[2])
    Lista[x].append((y, z))
    Lista[y].append((x, z))
    Matriz[x][y] = 1
    Matriz[y][x] = 1

print("-----Matriz-----")
for i in range(len(Matriz)):
    print(Matriz[i])
print("-----Lista-----")
print(Lista)


arq.close()