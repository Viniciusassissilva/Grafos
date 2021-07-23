import statistics as stt
import time
import os
import psutil
import matplotlib.pyplot as grafico

def gerar_Grafico(Graus):
    grafico.xlabel("Vertice")
    grafico.ylabel("Grau")
    grafico.axis(ymin=0, ymax=max(Graus))
    grafico.axis(xmin=0, xmax=len(Graus))
    grafico.plot(Graus)
    grafico.show()


def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

## https://qastack.com.br/programming/938733/total-memory-used-by-python-process
def lista(arq):
    memoryStart = get_process_memory()
    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = int(FirstLine[1])

    Lista = [[] for x in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = int(Aresta[2])
        Lista[x].append((y, z))
        Lista[y].append((x, z))

    memoryEnd = get_process_memory()
    Memoria = (memoryEnd - memoryStart)/(1024*1024)
    print(Memoria, "MB")
    return Lista

def matriz(arq):
    memoryStart = get_process_memory()
    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = int(FirstLine[1])
    Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = int(Aresta[2])
        Matriz[x][y] = z
        Matriz[y][x] = z

    memoryEnd = get_process_memory()
    Memoria = (memoryEnd - memoryStart) / (1024 * 1024)
    print(Memoria, "MB")
    return Matriz

def informacoes(Grafo, tipo):
    #Guarda o maior e o menos grau
    MaiorG = 0
    MenorG = len(Grafo)
    #Guarda o Vertice que possui o maior e menor grau
    VerticeMaiorG = 0
    VerticeMenorG = 0
    #Guarda o grau de cada vertice
    Graus = []
    #Tipo 1 é utilizado para Matriz
    if tipo == 1:
        for i in range(len(Grafo)):
            # cont salva o valor de cada linha no Grafo, que representa por sua vez cada vertice
            cont = len(Grafo[i]) - Grafo[i].count(0)
            Graus.append(cont)
            if MaiorG < cont:
                MaiorG = cont
                VerticeMaiorG = i
            if MenorG > cont:
                MenorG = cont
                VerticeMenorG = i
        print("Matriz de Adjacência")
    #Tipo 2 é utilizado para Lista
    elif tipo == 2:
        for i in range(len(Grafo)):
            Graus.append(len(Grafo[i]))
            if MaiorG < len(Grafo[i]):
                MaiorG = len(Grafo[i])
                VerticeMaiorG = i
            if MenorG > len(Grafo[i]):
                MenorG = len(Grafo[i])
                VerticeMenorG = i

        print("Lista de Adjacência")
    else:
        print("Escolha o Tipo correto!")

    print("Maior grau: %d -- vertice: %d \n"
          "Menor grau: %d -- vertice: %d \n"
          "\nGrau medio: %.7f" % (MaiorG, VerticeMaiorG, MenorG, VerticeMenorG, stt.mean(Graus)))
    print("\nFrequencia relativa:")
    #Calcula a frequencia de cada grau
    for i in sorted(set(Graus)):
        Frequencia = Graus.count(i) / len(Graus)
        print("Grau %d: %.7f " % (i, Frequencia))
    return Graus
# def informacoes_Geral(Grafo, tipo):
#
#     MaiorG = 0
#     MenorG = len(Grafo)
#     #MenorG = float("inf")
#
#     VerticeMaiorG = 0
#     VerticeMenorG = 0
#
#     if tipo == 1:
#         for i in range(len(Grafo)):
#             cont = 0
#             for x in range(len(Grafo[i])):
#                 if Grafo[i][x] != 0:
#                     cont = cont + 1
#             if MaiorG < cont:
#                 MaiorG = cont
#                 VerticeMaiorG = i
#             if MenorG > cont:
#                 MenorG = cont
#                 VerticeMenorG = i
#         print("Matriz de Adjacência")
#     elif tipo == 2:
#         for i in range(len(Grafo) - 1):
#             if MaiorG < len(Grafo[i]):
#                 MaiorG = len(Grafo[i])
#                 VerticeMaiorG = i
#             if MenorG > len(Grafo[i]):
#                 MenorG = len(Grafo[i])
#                 VerticeMenorG = i
#
#         print("Lista de Adjacência")
#     else:
#         print("Escolha o Tipo correto!")
#
#     print("Maior grau: %d -- vertice: %d \n"
#           "Menor grau: %d -- vertice: %d" % (MaiorG, VerticeMaiorG, MenorG, VerticeMenorG))

def busca_Largura(Grafo, VInicial, tipo):

    if tipo == 1:
        start = time.time()
        print("Matriz")
        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1

        while len(Q) != 0:

            u = Q.pop(0)
            for v in range(len(Grafo)):
                if Grafo[u][v] != 0:
                    if desc[v] == 0:
                        Q.append(v)
                        R.append(v)
                        desc[v] = 1

        End  = time.time()
        print(End - start, "milesegundos")
        return R
    elif tipo == 2:
        start = time.time()
        print("Lista")
        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1

        while len(Q) != 0:

            u = Q.pop(0)
            for v in Grafo[u]:
                if v != []:
                    if desc[v[0]] == 0:
                        Q.append(v[0])
                        R.append(v[0])
                        desc[v[0]] = 1
        End = time.time()
        print(End - start, "milesegundos")
        return R

    else:
        print("Escolha o Tipo correto!")

def busca_Profundidade(Grafo, VInicial, tipo):
    if tipo == 1:
        start = time.time()
        print("Matriz")
        desc = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1

        while len(S) != 0:
            u = S[-1]
            desempilhar = True

            for v in range(len(Grafo[u])):
                if Grafo[u][v] != 0:
                    if desc[v] == 0:
                        desempilhar = False
                        S.append(v)
                        R.append(v)
                        desc[v] = 1
                        break

            if desempilhar:
                S.pop()
        End = time.time()
        print(End - start, "milesegundos")
        return R
    elif tipo == 2:
        start = time.time()
        print("Lista")
        desc = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        while len(S) != 0:
            u = S[-1]
            desempilhar = True

            for v in Grafo[u]:
                if v != []:
                    if desc[v[0]] == 0:
                        desempilhar = False
                        S.append(v[0])
                        R.append(v[0])
                        desc[v[0]] = 1
                        break
            if desempilhar:
                S.pop()
        End = time.time()
        print(End - start, "milesegundos")
        return R
    else:
        print("Escolha o Tipo correto!")

def busca_Largura_Nivel(Grafo, VInicial, tipo):

    if tipo == 1:
        print("Matriz")
        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        nivel = [0 for i in range(len(Grafo))]#Cria lista de niveis
        nivel[VInicial] = 0 #grava o nivel inicial
        realmenor = [] #auxiliar pra guardar o menor nivel que esta ligado o vertice

        while len(Q) != 0:

            u = Q.pop(0)
            for i in range(len(Grafo[u])): #percorre a linha u da matriz
                if Grafo[u][i] != 0:
                    if desc[i] == 0:
                        nivel[i] = nivel[u] + 1

            for v in range(len(Grafo)):
                if Grafo[u][v] != 0:
                    if desc[v] == 0:
                        Q.append(v)
                        R.append(v)
                        desc[v] = 1

        for i in range(len(desc)):
            if desc[i] == 0 and i != VInicial:
                for x in range(len(Grafo[i])):
                    if Grafo[i][x] != 0:
                        if x in R:
                            nivel[i] = nivel[x] + 1
                            realmenor.append(nivel[i])
            if len(realmenor) > 1:
                for x in range(len(realmenor) - 1):
                    if realmenor[x] < realmenor[x + 1]:
                        nivel[i] = realmenor[x + 1]

        arquivo = open("saida.txt", "w")
        arquivo.write("#vertice : nivel \n")
        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                arquivo.write("%d : %d \n" % (i, nivel[i]))
        return nivel
    elif tipo == 2:
        print("Lista")

        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        nivel = [0 for i in range(len(Grafo))]
        nivel[VInicial] = 0

        while len(Q) != 0:

            u = Q.pop(0)

            for i in range(len(Grafo[u])):

                if desc[Grafo[u][i][0]] == 0:
                    nivel[Grafo[u][i][0]] = nivel[u] + 1

            for v in range(len(Grafo[u])):
                if desc[Grafo[u][v][0]] == 0:
                    Q.append(Grafo[u][v][0])
                    R.append(Grafo[u][v][0])
                    desc[Grafo[u][v][0]] = 1

        for i in range(len(desc)):
            if desc[i] == 0 and i != VInicial:
                for x in range(len(Grafo[i])):
                    if Grafo[i][x][0] in R:
                        if len(Grafo[i]) > 1:
                            if nivel[i] == 0:
                                nivel[i] = nivel[Grafo[i][x][0]] + 1
                            elif nivel[i] > nivel[Grafo[i][x][0]] + 1:
                                nivel[i] = nivel[Grafo[i][x][0]] + 1
                        else:
                            nivel[i] = nivel[Grafo[i][x][0]] + 1

        arquivo = open("saida.txt", "w")
        arquivo.write("#vertice : nivel \n")
        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                arquivo.write("%d : %d \n" % (i, nivel[i]))
        return nivel

    else:
        print("Escolha o Tipo correto!")

def busca_Profundidade_Nivel(Grafo, VInicial, tipo):

    if tipo == 1:
        print("Matriz")
        desc = [0 for i in range(len(Grafo))]
        nivel = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        nivel[VInicial] = 0

        while len(S) != 0:
            u = S[-1]
            desempilhar = True

            for v in range(len(Grafo[u])):
                if Grafo[u][v] != 0:
                    if nivel[v] == 0 and v != VInicial:
                        nivel[v] = nivel[u] + 1
                    for x in range(len(Grafo[v])):
                        if Grafo[v][x] != 0:
                            if nivel[x] <= nivel[v] and nivel[v] == 0 and v != VInicial:
                                nivel[v] = nivel[x] + 1

            for v in range(len(Grafo[u])):
                if Grafo[u][v] != 0:
                    if desc[v] == 0:
                        desempilhar = False
                        S.append(v)
                        R.append(v)
                        desc[v] = 1
                        break

            if desempilhar:
                S.pop()
        for i in range(len(desc)):
            if desc[i] == 0 and i != VInicial:
                for v in range(len(Grafo[i])):
                    if Grafo[i][v] != 0:
                        if v in R:
                            if nivel[i] == 0:
                                nivel[i] = nivel[v] + 1
                            elif nivel[i] > nivel[v] + 1:
                                nivel = nivel[v] + 1

        arquivo = open("saida.txt", "w")
        arquivo.write("#vertice : nivel \n")
        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                arquivo.write("%d : %d \n" % (i, nivel[i]))
        return nivel
    elif tipo == 2:
        print("Lista")
        desc = [0 for i in range(len(Grafo))]
        nivel = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        nivel[VInicial] = 0
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for i in Grafo[u]:
                if i != []:
                    if nivel[i[0]] == 0 and i[0] != VInicial:
                        nivel[i[0]] = nivel[u] + 1

            for v in Grafo[u]:
                if v != []:
                    if desc[v[0]] == 0:
                        desempilhar = False
                        S.append(v[0])
                        R.append(v[0])
                        desc[v[0]] = 1
                        break
            if desempilhar:
                S.pop()

        # #Tratamento para grafos orientados
        menor = len(Grafo)
        for i in range(len(desc)):
            if desc[i] == 0 and i in R:  # identifica os não descobertos
                for x in Grafo[i]:  # identifica para onde o vertice aponta
                    if x != []:
                        if nivel[x[0]] < menor and x[0] != VInicial:
                            menor = nivel[x[0]]
                            nivel[i] = nivel[x[0]] + 1

        arquivo = open("saida.txt", "w")
        arquivo.write("#vertice : nivel \n")
        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                arquivo.write("%d : %d \n" % (i, nivel[i]))
        return R
    else:
        print("Escolha o Tipo correto!")

def conexo_principal(Grafo, tipo, VInicial = 0):

    Maior = 0
    Menor = len(Grafo)

    if tipo == 1:
        print("Matriz")
        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        count = 0
        conexo = 0

        while len(Q) != 0:

            u = Q.pop(0)

            for v in range(len(Grafo)):
                if Grafo[u][v] != 0:
                    if desc[v] == 0:
                        Q.append(v)
                        R.append(v)
                        desc[v] = 1

        if Maior < len(R):
            Maior = len(R)
        if Menor > len(R):
            Menor = len(R)
        vprint = []  ##Guarda as componentes conexas
        vprint.append("-- %d vertices" % (len(R)))
        for v in range(len(desc)):
            if desc[v] == 0:
                count = count + 1
                for x in R:
                    if Grafo[x][v] != 0 or Grafo[v][x]:
                        conexo = conexo + 1
                        break
            if count != conexo and desc[v] == 0:  ##Descobre quando a componente não conexa existe
                ##Funçao similiar para conseguir fazer a busca recursiva
                ##Retira dois paramentros e adiciona dois
                ##Passa os descobertos e a lista com os descobertos(String)
                Q = [v]
                R = [v]
                desc[v] = 1
                while len(Q) != 0:

                    u = Q.pop(0)

                    for v in range(len(Grafo)):
                        if Grafo[u][v] != 0:
                            if desc[v] == 0:
                                Q.append(v)
                                R.append(v)
                                desc[v] = 1
                if Maior < len(R):
                    Maior = len(R)
                if Menor > len(R):
                    Menor = len(R)
                vprint.append("-- %d vertices" % (len(R)))
        print("%d - Vertices ---- Maior componente conexa \n"
              "%d - Vertices ---- Menor componente conexa \n" % (Maior, Menor))
        print("Componentes conexas: %d" % (len(vprint)))
        for i in vprint:
            print(i)
    elif tipo == 2:
        print("Lista")
        desc = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        count = 0
        conexo = 0

        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for v in range(len(Grafo[u])):
                if desc[Grafo[u][v][0]] == 0:
                    desempilhar = False
                    S.append(Grafo[u][v][0])
                    R.append(Grafo[u][v][0])
                    desc[Grafo[u][v][0]] = 1
                    break
            if desempilhar:
                S.pop()
        if Maior < len(R):
            Maior = len(R)
        if Menor > len(R):
            Menor = len(R)
        vprint = [] ##Guarda as componentes conexas
        vprint.append("-- %d vertices" % (len(R)))
        for v in range(len(desc)):
            if desc[v] == 0:
                count = count + 1
                for x in R:
                    for i in range(len(Grafo[v])):
                        if x == Grafo[v][i][0]:
                            conexo = conexo + 1
                            break
            if count != conexo and desc[v] == 0: ##Descobre quando a componente não conexa existe
                ##Funçao similiar para conseguir fazer a busca recursiva
                ##Retira dois paramentros e adiciona dois
                ##Passa os descobertos e a lista com os descobertos(String)
                S = [v]
                R = [v]
                desc[v] = 1
                while len(S) != 0:
                    u = S[-1]
                    desempilhar = True
                    for v in range(len(Grafo[u])):
                        if desc[Grafo[u][v][0]] == 0:
                            desempilhar = False
                            S.append(Grafo[u][v][0])
                            R.append(Grafo[u][v][0])
                            desc[Grafo[u][v][0]] = 1
                            break
                    if desempilhar:
                        S.pop()
                if Maior < len(R):
                    Maior = len(R)
                if Menor > len(R):
                    Menor = len(R)
                vprint.append("-- %d vertices" % (len(R)))

        print("%d - Vertices ---- Maior componente conexa \n"
              "%d - Vertices ---- Menor componente conexa \n" % (Maior, Menor))
        print("Componentes conexas: %d" % (len(vprint)))
        for i in vprint:
            print(i)
    else:
        print("Escolha o Tipo correto!")

