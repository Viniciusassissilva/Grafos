import Funcoes
def Sub_Menu_1():
    print("Escolha uma opção entre 0 e 3! \n"
          "0 : Sair\n"
          "1 : Parte 1 do Trabalho \n"
          "2 : Parte 2 do Trabalho (Grafo de Colaborações em Pesquisa.) \n"
          "3 : Parte 3 do Trabalho (Grafo de Conexções da Web.)\n")
def Sub_Menu_11():
    print("Parte 01: \n"
          "0 : Menu anterior\n"
          "1 : Trocar arquivo de Entrada \n"
          "2 : Represetação do Grafo \n"
          "3 : Informações do Grafo \n"
          "4 : Nivel de cada vertice \n"
          "5 : Componentes Conexos \n")
def Sub_Menu_111():
    print("Trocar arquivo de Entrada\n"
          "0 : Menu anterior\n"
          "1 : collaboration_graph.txt\n"
          "2 : as_graph.txt\n")
def Sub_Menu_112():
    print("Informações do Grafo\n"
          "0 : Menu anterior\n"
          "1 : Matriz\n"
          "2 : Lista\n")
def Sub_Menu_113():
    print("Nivel de cada vertice\n"
          "0 : Menu anterior\n"
          "1 : Lista por largura\n"
          "2 : Lista por profundidade\n"
          "3 : Matriz por largura\n"
          "4 : Matriz por profundidade\n")
def Sub_Menu_114():
    print("Componentes Conexos\n"
          "0 : Menu anterior\n"
          "1 : Matriz\n"
          "2 : Lista\n")
def Sub_Menu_12():
    print("Menu: \n"
          "0 : Menu anterior\n"
          "1 : Compara desempenho em custo de memoria Lista x Matriz \n"
          "2 : Compara desempenho em tempo de execução Lista x Matriz \n"
          "3 : Distribuição empirica \n"
          "4 : Componente conexo \n")
def Sub_Menu_121():
    print("Compara desempenho em custo de memoria Lista x Matriz: \n"
          "0 : Menu anterior\n"
          "1 : Desempenho Lista \n"
          "2 : Desempenho Matriz \n")
def Sub_Menu_122():
    print("Compara desempenho em tempo de execução Lista x Matriz: \n"
          "0 : Menu anterior\n"
          "1 : Busca Largura Lista \n"
          "2 : Busca Profundidade Lista \n"
          "3 : Busca Largura Matriz \n"
          "4 : Busca Profundidade Matriz \n")
def Sub_Menu_123():
    print("Distribuição empirica: \n"
          "0 : Menu anterior\n"
          "1 : Lista \n"
          "2 : Matriz \n")

def Sub_Menu_124():
    print("Componente conexo: \n"
          "0 : Menu anterior\n"
          "1 : Lista \n"
          "2 : Matriz \n")
def Sub_Menu_13():
    print("Menu: \n"
          "1 : Distribuição Empirica \n"
          "2 : Componentes conexas \n"
          "3 : Informações do Grafo \n"
          "4 : Nivel de cada vertice \n"
          "5 : Componentes Conexos \n")

def Menu_():

    print("Por padrão o arquivo de entrada é definido pelo arquivo teste: Entrada_Test.txt ")
    arq = open('Entrada_Test.txt', 'r')
    Lista = Funcoes.lista(arq)
    Matriz = Funcoes.matriz(arq)
    Sub_Menu_1()
    menu1 = int(input('Opcão: '))

    while menu1 != 0:
        if menu1 == 1:
            Sub_Menu_11()
            menu2 = int(input('Opcão: '))
            while menu2 != 0:
                if menu2 == 1:
                    Sub_Menu_111()
                    menu3 = int(input("Opção: "))
                    while menu3 != 0:
                        if menu3 == 1:
                            arq = open('collaboration_graph.txt', 'r')
                            Lista = Funcoes.lista(arq)
                            Matriz = Funcoes.matriz(arq)
                            menu3 = -1
                        elif menu3 == 2:
                            arq = open('as_graph.txt', 'r')
                            Lista = Funcoes.lista(arq)
                            Matriz = Funcoes.matriz(arq)
                            menu3 = -1
                        else:
                            Sub_Menu_111()
                            menu3 = int(input("Opção: "))
                    menu2 = -1
                    print()
                elif menu2 == 2:
                    for i in range(len(Lista)):
                        if i == 0:
                            print("L =",Lista[i])
                        else:
                            print("   ",Lista[i])
                    for i in range(len(Matriz)):
                        if i == 0:
                            print("M =",Matriz[i])
                        else:
                            print("   ",Matriz[i])
                    menu2 = -1
                    print()
                elif menu2 == 3:
                    Sub_Menu_112()
                    menu3 = int(input("Opção: "))
                    while menu3 != 0:
                        if menu3 == 1:
                            Funcoes.informacoes(Matriz, 1)
                            menu3 = -1
                            print()
                        elif menu3 == 2:
                            Funcoes.informacoes(Lista, 2)
                            menu3 = -1
                            print()
                        else:
                            Sub_Menu_112()
                            menu3 = int(input("Opção: "))
                    menu2 = -1
                    print()
                elif menu2 == 4:
                    Sub_Menu_113()
                    menu3 = int(input("Opção: "))
                    while menu3 != 0:
                        if menu3 == 1:
                            Funcoes.busca_Largura_Nivel(Lista, 0, 2)
                            menu3 = -1
                            print()
                        elif menu3 == 2:
                            Funcoes.busca_Profundidade_Nivel(Lista, 0, 2)
                            menu3 = -1
                            print()
                        elif menu3 == 3:
                            Funcoes.busca_Largura_Nivel(Matriz, 0, 1)
                            menu3 = -1
                            print()
                        elif menu3 == 4:
                            Funcoes.busca_Profundidade_Nivel(Matriz, 0, 1)
                            menu3 = -1
                            print()
                        else:
                            Sub_Menu_113()
                            menu3 = int(input("Opção: "))
                    menu2 = -1
                    print()
                elif menu2 == 5:
                    Sub_Menu_114()
                    menu3 = int(input("Opção: "))
                    while menu3 != 0:
                        if menu3 == 1:
                            Funcoes.conexo_principal(Matriz, 1, 0)
                            menu3 = -1
                            print()
                        elif menu3 == 2:
                            Funcoes.conexo_principal(Lista, 2, 0)
                            menu3 = -1
                            print()
                        else:
                            Sub_Menu_114()
                            menu3 = int(input("Opção: "))
                    menu2 = -1
                    print()
                else:
                    Sub_Menu_11()
                    menu2 = int(input('Opcão: '))
            if menu2 == 0:
                menu1 = -1
        elif menu1 == 2:
            Sub_Menu_12()
            menu2 = int(input('Opcão: '))
            while menu2 != 0:
                if menu2 == 1:
                    Sub_Menu_121()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            arq = open('collaboration_graph.txt', 'r')
                            Lista = Funcoes.lista(arq)
                            menu3 = -1
                        elif menu3 == 2:
                            arq = open('collaboration_graph.txt', 'r')
                            Matriz = Funcoes.matriz(arq)
                            menu3 = -1
                        else:
                            Sub_Menu_121()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                elif menu2 == 2:
                    Sub_Menu_122()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            Funcoes.busca_Largura(Lista, 1, 2)
                            menu3 = -1
                        elif menu3 == 2:
                            Funcoes.busca_Profundidade(Lista,1,2)
                            menu3 = -1
                        elif menu3 == 3:
                            Funcoes.busca_Largura(Matriz, 1, 1)
                            menu3 = -1
                        elif menu3 == 4:
                            Funcoes.busca_Profundidade(Matriz,1,1)
                            menu3 = -1
                        else:
                            Sub_Menu_122()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                elif menu2 == 3:
                    Sub_Menu_123()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            Grau = Funcoes.informacoes(Lista, 2)
                            Funcoes.gerar_Grafico(Grau)
                            menu3 = -1
                        elif menu3 == 2:
                            Grau = Funcoes.informacoes(Matriz, 1)
                            Funcoes.gerar_Grafico(Grau)
                            menu3 = -1
                        else:
                            Sub_Menu_123()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                elif menu2 == 4:
                    Sub_Menu_124()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            Funcoes.conexo_principal(Lista, 2)
                            menu3 = -1
                        elif menu3 == 2:
                            Funcoes.conexo_principal(Matriz, 1)
                            menu3 = -1
                        else:
                            Sub_Menu_124()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                else:
                    Sub_Menu_12()
                    menu2 = int(input('Opcão: '))
            if menu2 == 0:
                menu1 = -1
        elif menu1 == 3:
            Sub_Menu_12()
            menu2 = int(input('Opcão: '))
            while menu2 != 0:
                if menu2 == 1:
                    Sub_Menu_121()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            arq = open('collaboration_graph.txt', 'r')
                            Lista = Funcoes.lista(arq)
                            menu3 = -1
                        elif menu3 == 2:
                            arq = open('collaboration_graph.txt', 'r')
                            Matriz = Funcoes.matriz(arq)
                            menu3 = -1
                        else:
                            Sub_Menu_121()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                elif menu2 == 2:
                    Sub_Menu_122()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            Funcoes.busca_Largura(Lista, 1, 2)
                            menu3 = -1
                        elif menu3 == 2:
                            Funcoes.busca_Profundidade(Lista, 1, 2)
                            menu3 = -1
                        elif menu3 == 3:
                            Funcoes.busca_Largura(Matriz, 1, 1)
                            menu3 = -1
                        elif menu3 == 4:
                            Funcoes.busca_Profundidade(Matriz, 1, 1)
                            menu3 = -1
                        else:
                            Sub_Menu_122()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                elif menu2 == 3:
                    Sub_Menu_123()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            Grau = Funcoes.informacoes(Lista, 2)
                            Funcoes.gerar_Grafico(Grau)
                            menu3 = -1
                        elif menu3 == 2:
                            Grau = Funcoes.informacoes(Matriz, 1)
                            Funcoes.gerar_Grafico(Grau)
                            menu3 = -1
                        else:
                            Sub_Menu_123()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                elif menu2 == 4:
                    Sub_Menu_124()
                    menu3 = int(input('Opcão: '))
                    while menu3 != 0:
                        if menu3 == 1:
                            Funcoes.conexo_principal(Lista, 2)
                            menu3 = -1
                        elif menu3 == 2:
                            Funcoes.conexo_principal(Matriz, 1)
                            menu3 = -1
                        else:
                            Sub_Menu_124()
                            menu3 = int(input('Opcão: '))
                    menu2 = -1
                    print()
                else:
                    Sub_Menu_12()
                    menu2 = int(input('Opcão: '))
            if menu2 == 0:
                menu1 = -1
            break
        else:
            Sub_Menu_1()
            menu1 = int(input('Opcão: '))

Menu_()