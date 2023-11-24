import networkx as nx

# Definir constante para escolher o vértice de origem e de saída
S = 1
T = 5

# Método Ford Fulkerson
def ford_fulkerson(grafo, origem, destino):
    fluxo_maximo = 0
    fluxo_elementar = []

    # Busca em profundidade
    while True:
        fila = [origem]
        caminho = {origem: None}
        visitados = {origem}

        while fila:
            node = fila.pop(0)
            if node == destino:
                break

            for vizinho, dados in grafo[node].items():
                capacidade = dados['capacidade']
                if vizinho not in visitados and capacidade > 0:
                    visitados.add(vizinho)
                    fila.append(vizinho)
                    caminho[vizinho] = node

        if destino not in visitados:
            break

        fluxo = float("inf")
        v = destino
        caminho_atual = []
        while v != origem:
            u = caminho[v]
            fluxo = min(fluxo, grafo[u][v]['capacidade'])
            caminho_atual.append((u, v))
            v = u

        fluxo_maximo += fluxo
        fluxo_elementar.append((caminho_atual, fluxo))

        v = destino
        while v != origem:
            u = caminho[v]
            grafo[u][v]['capacidade'] -= fluxo
            grafo[v][u]['capacidade'] += fluxo
            v = u

    return fluxo_maximo, fluxo_elementar

# Analisar input
grafo = nx.DiGraph()
with open('grafo1.txt', 'r') as arquivo:
    for linha in arquivo:
        origem, alvo, capacidade = map(int, linha.split())
        if not grafo.has_edge(origem, alvo):
            grafo.add_edge(origem, alvo, capacidade=0)
        if not grafo.has_edge(alvo, origem):
            grafo.add_edge(alvo, origem, capacidade=0)
        grafo[origem][alvo]['capacidade'] += capacidade

fluxo_maximo, fluxo_elementar = ford_fulkerson(grafo, S, T)
print("Fluxo Máximo: ", fluxo_maximo)
print("Fluxo Elementar: ")
for caminho, fluxo in fluxo_elementar:
    print(f"Caminho: {caminho}, Fluxo: {fluxo}")
