from classes import *

def lerInput(entrada):
    grafo = Grafo()
    
    with open(entrada, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip().split()
            if len(linha) == 2:
                vertice_origem, vertice_destino = linha
                grafo.addVertice(vertice_origem)
                grafo.addVertice(vertice_destino)
                grafo.addAresta(vertice_origem, vertice_destino)
            else:
                print(".")
    
    return grafo
