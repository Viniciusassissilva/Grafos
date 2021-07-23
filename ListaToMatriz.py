
def retornaMatriz(lista):

    M = [[0 for _ in range(len(lista))] for _ in range(len(lista))]

    for x in range(len(lista)):
        for j in range(len(lista[x])):
            M[x][lista[x][j]] = 1

    return M

