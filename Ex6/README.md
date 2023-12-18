# Coloração de Grafos - 8 Rainhas

Este é um programa em Python que resolve o problema das 8 Rainhas usando coloração de grafos

## Entrada

O programa lê um arquivo GML contendo um grafo que representa o tabuleiro. O caminho do arquivo GML é especificado diretamente no código:

```
arquivo = "input.gml"
```

## Saída

A saída do programa é a posição das rainhas no tabuleiro que resolve o problema. O tabuleiro resultante é impresso na saída padrão. No caso desse input, a saída é essa:

```
Q . . . . . . . 
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
```

Se não houver uma solução, o programa imprime:

```
"Nenhuma solução encontrada."
```

## Dependências

```
pip install networkx
```

## Compilação e Execução

```
python main.py
```





