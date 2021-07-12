import statistics as stt

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
            #cont salva o valor de cada linha no Grafo, que representa por sua vez cada vertice
            cont = sum(Grafo[i])
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
          "\nGrau medio: %.2f" % (MaiorG, VerticeMaiorG, MenorG, VerticeMenorG, stt.mean(Graus)))
    print("\nFrequencia relativa:")
    #Calcula a frequencia de cada grau
    for i in sorted(set(Graus)):
        Frequencia = Graus.count(i) / len(Graus)
        print("Grau %d: %.2f " % (i, Frequencia))

def informacoes_Geral(Grafo, tipo):

    MaiorG = 0
    MenorG = len(Grafo)

    VerticeMaiorG = 0
    VerticeMenorG = 0

    if tipo == 1:
        for i in range(len(Grafo)):
            cont = 0
            for x in range(len(Grafo[i])):
                if Grafo[i][x] != 0:
                    cont = cont + 1
            if MaiorG < cont:
                MaiorG = cont
                VerticeMaiorG = i
            if MenorG > cont:
                MenorG = cont
                VerticeMenorG = i
        print("Matriz de Adjacência")
    elif tipo == 2:
        for i in range(len(Grafo) - 1):
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
          "Menor grau: %d -- vertice: %d" % (MaiorG, VerticeMaiorG, MenorG, VerticeMenorG))

def busca_Largura(Grafo, VInicial, tipo):

    if tipo == 1:
        print("Matriz")
        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        nivel = [0 for i in range(len(Grafo))]
        nivel[VInicial] = 0
        realmenor = []

        while len(Q) != 0:

            u = Q.pop(0)
            for i in range(len(Grafo[u])):
                if Grafo[u][i] == 1:
                    if desc[i] == 0:
                        nivel[i] = nivel[u] + 1

            for v in range(len(Grafo)):
                if Grafo[u][v] == 1:
                    if desc[v] == 0:
                        Q.append(v)
                        R.append(v)
                        desc[v] = 1

        for i in range(len(desc)):
            if desc[i] == 0 and i != VInicial:
                for x in range(len(Grafo[i])):
                    if Grafo[i][x] == 1:
                        if x in R:
                            nivel[i] = nivel[x] + 1
                            realmenor.append(nivel[i])
            if len(realmenor) > 1:
                for x in range(len(realmenor) - 1):
                    if realmenor[x] < realmenor[x + 1]:
                        nivel[i] = realmenor[x + 1]

        print("#vertice : nivel")

        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                print("%d : %d" % (i, nivel[i]))

        return nivel
    elif tipo == 2:
        print("Lista")

    else:
        print("Escolha o Tipo correto!")

def busca_Profundidade(Grafo, VInicial, tipo):

    if tipo == 1:
        print("Matriz")
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
                if desc[i] == 0:
                    nivel[i] = nivel[u] + 1  # cada elemento nao descorbeto em "u" está um nivel abaixo dele
                    for x in range(len(Grafo[i]) - 1):  # identifica para onde o vertice aponta
                        if len(Grafo[i]) > 1:  # Compara dois vertices
                            if nivel[Grafo[i][x]] <= nivel[Grafo[i][x + 1]] and nivel[i] == 0:
                                nivel[i] = nivel[Grafo[i][x]] + 1  # Coloca ele um nivel abaixo do menor nivel que ele liga
                        elif len(Grafo[i]) == 1:  # Se apontar para apenas um vertice
                            nivel[i] = nivel[Grafo[i][x]] + 1  # Coloca ele um nivel abaixo do menor nivel que ele liga

            for v in Grafo[u]:
                if desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
            if desempilhar:
                S.pop()

        ##Tratamento para grafos orientados
        for i in range(len(desc)):
            if desc[i] == 0:  # identifica os não descobertos
                for x in range(len(Grafo[i]) - 1):  # identifica para onde o vertice aponta
                    if Grafo[i][x] in R:  # Verifica se é conexo
                        if len(Grafo[i]) > 1:  # Compara dois vertices
                            if nivel[Grafo[i][x]] <= nivel[Grafo[i][x + 1]] and nivel[i] == 0:
                                nivel[i] = nivel[Grafo[i][x]] + 1  # Coloca ele um nivel abaixo do menor nivel que ele liga
                        elif len(Grafo[i]) == 1:  # Se apontar para apenas um vertice
                            nivel[i] = nivel[Grafo[i][x]] + 1  # Coloca ele um nivel abaixo do menor nivel que ele liga

        print("#vertice : nivel")
        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                print("%d : %d" % (i, nivel[i]))
        return nivel
    else:
        print("Escolha o Tipo correto!")

def conexo_principal(Grafo, tipo, VInicial = 0):

    if tipo == 1:
        print("Matriz")
    elif tipo == 2:
        desc = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        count = 0
        conexo = 0

        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for v in Grafo[u]:
                if desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    break
            if desempilhar:
                S.pop()

        vprint = [] ##Guarda as componentes conexas
        vprint.append("-- %d vertices" % (len(R)))
        for v in range(len(desc)):
            if desc[v] == 0:
                count = count + 1
                for x in R:
                    if x in Grafo[v]:
                        conexo = conexo + 1
                        break
            if count != conexo and 0 in desc: ##Descobre quando a componente não conexa existe
                ##Funçao similiar para conseguir fazer a busca recursiva
                ##Retira dois paramentros e adiciona dois
                ##Passa os descobertos e a lista com os descobertos(String)
                conexo_outros(Grafo, v, desc, vprint)

        print("Componentes conexas: %d" % (len(vprint)))
        for i in vprint:
            print(i)
    else:
        print("Escolha o Tipo correto!")

def conexo_outros(Grafo, s, desc, vprint):
    ##Função auxiliar
    S = [s]
    R = [s]
    desc[s] = 1
    count = 0
    conexo = 0

    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v in Grafo[u]:
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                break

        if desempilhar:
            S.pop()

    vprint.append("-- %d vertices" % (len(R)))
    for v in range(len(desc)):
        if desc[v] == 0:
            count = count + 1
            for x in R:
                if x in Grafo[v]:
                    conexo = conexo + 1
                    break
        if count != conexo and 0 in desc:
            conexo_outros(Grafo, v, desc, vprint)



def desempenho(Grafo, tipo):

    if tipo == 1:
        print("Matriz")
    elif tipo == 2:
        print("Lista")
    else:
        print("Escolha o Tipo correto!")

def distribuicao_Impirica(Grafo, tipo):

    if tipo == 1:
        print("Matriz")
    elif tipo == 2:
        print("Lista")
    else:
        print("Escolha o Tipo correto!")