from functions import *

entrada = 'input.txt'
grafo = lerInput(entrada)

for nome, vertice in grafo.vertices.items():
    print(f"Vértice: {nome}, Vizinhos: {', '.join(vertice.vizinhos)}")

componentesfconexas = grafo.fConexas()
for i, componente in enumerate(componentesfconexas):
    print(f"Componente f-conexa {i + 1}: {', '.join(componente)}")

