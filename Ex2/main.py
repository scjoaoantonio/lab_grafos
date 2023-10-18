import networkx as nx

def calcular_pert(grafo):
    tempos_mais_cedo = nx.topological_sort(grafo)
    for node in tempos_mais_cedo:
        max_tempo_mais_cedo = 0
        for predecessor in grafo.predecessors(node):
            max_tempo_mais_cedo = max(max_tempo_mais_cedo, grafo.nodes[predecessor]['tempo_mais_cedo'] + grafo[predecessor][node]['peso'])
        grafo.nodes[node]['tempo_mais_cedo'] = max_tempo_mais_cedo

    tempos_mais_tarde = list(reversed(list(nx.topological_sort(grafo))))
    for node in tempos_mais_tarde:
        if not list(grafo.successors(node)): 
            grafo.nodes[node]['tempo_mais_tarde'] = grafo.nodes[node]['tempo_mais_cedo']
        else:
            min_tempo_mais_tarde = float('inf')
            for successor in grafo.successors(node):
                min_tempo_mais_tarde = min(min_tempo_mais_tarde, grafo.nodes[successor]['tempo_mais_tarde'] - grafo[node][successor]['peso'])
            grafo.nodes[node]['tempo_mais_tarde'] = min_tempo_mais_tarde

    caminho_critico = []
    for edge in grafo.edges():
        if grafo.nodes[edge[0]]['tempo_mais_cedo'] == grafo.nodes[edge[1]]['tempo_mais_tarde'] - grafo[edge[0]][edge[1]]['peso']:
            caminho_critico.append(edge)

    return tempos_mais_cedo, tempos_mais_tarde, caminho_critico

with open('input.txt', 'r') as file:
    linhas = file.readlines()

G = nx.DiGraph()

for linha in linhas:
    dados = linha.split()
    origem = int(dados[0])
    destino = int(dados[1])
    peso = int(dados[2])
    G.add_edge(origem, destino, peso=peso)

for node in G.nodes():
    if not list(G.predecessors(node)):
        G.nodes[node]['tempo_mais_cedo'] = 0

tempos_mais_cedo, tempos_mais_tarde, caminho_critico = calcular_pert(G)

print("Tempos mais cedo:")
for node in G.nodes():
    print(f"Nó {node}: {G.nodes[node]['tempo_mais_cedo']}")

print("\nTempos mais tarde:")
for node in tempos_mais_tarde:
    print(f"Nó {node}: {G.nodes[node]['tempo_mais_tarde']}")

print("\nCaminho crítico:")
for edge in caminho_critico:
    print(f"Atividade de {edge[0]} para {edge[1]} com duração {G[edge[0]][edge[1]]['peso']}")
