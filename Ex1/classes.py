class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []
        self.cor = None
        self.visitado = False

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def addVertice(self, nome):
        if nome not in self.vertices:
            self.vertices[nome] = Vertice(nome)
    
    def addAresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].vizinhos.append(destino)
    
    def dfs(self, vertice):
        vertice.visitado = True
        componente = []
        componente.append(vertice.nome)

        for vizinho_nome in vertice.vizinhos:
            vizinho = self.vertices[vizinho_nome]
            if not vizinho.visitado:
                componente += self.dfs(vizinho)

        return componente

    def fConexas(self):
        componentesfconexas = []
        for nome, vertice in self.vertices.items():
            if not vertice.visitado:
                componente = self.dfs(vertice)
                componentesfconexas.append(componente)

        return componentesfconexas