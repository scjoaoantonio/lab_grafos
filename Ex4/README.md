# Algoritmo para Cobertura Mínima em Grafo

Este algoritmo em Python implementa a busca por uma cobertura mínima em um grafo que represanta algumas ruas de São João del Rei

## Entrada

O programa recebe como entrada um grafo no formato GML.
O nome do arquivo GML é fornecido diretamente no código.

```
nome_arquivo = "sjdr.gml"
```

## Saída

O resultado da execução é uma lista de vértices que formam a cobertura mínima do grafo.

```
print("\nCobertura mínima (vértices selecionados):\n\n", vertices_selecionados)
```

## Dependências

O código utiliza a biblioteca NetworkX para manipulação de grafos em Python. Você pode instalá-la utilizando o seguinte comando:

```
pip install networkx
```

## Compilação e Execução

```
python main.py
```
