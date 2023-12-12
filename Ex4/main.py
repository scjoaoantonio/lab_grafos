import networkx as nx

def cobertura_minimal(grafo):
    vertices_selecionados = []
    grafo_restante = grafo.copy()

    # enquanto tiver aresta que sem cobertura:
    while grafo_restante.edges:
        # acha o vértice que cobre o maximo de arestas não cobertas
        vertice_max_cobertura = max(grafo_restante.nodes, key=lambda x: len(list(grafo_restante.edges(x))))

        vertices_selecionados.append(vertice_max_cobertura)

        # remove as arestas cobertas pelo vértice selecionado do grafo restante
        arestas_cobertas = list(grafo_restante.edges(vertice_max_cobertura))
        grafo_restante.remove_edges_from(arestas_cobertas)

    return vertices_selecionados

grafo = nx.read_gml("sjdr.gml")
vertices_selecionados = cobertura_minimal(grafo)
print("\nCobertura mínima (esquinas selecionadas):\n\n", vertices_selecionados)
