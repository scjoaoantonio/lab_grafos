import networkx as nx

def ler_input(arquivo):
    G = nx.ler_input(arquivo)
    return G

def print_tabuleiro(resposta):
    for linha in resposta:
        line = ""
        for coluna in range(len(resposta)):
            if coluna == linha:
                line += "Q "
            else:
                line += ". "
        print(line)

def verifica(tabuleiro, linha, coluna):
    if any(tabuleiro[linha]):
        return False
    
    if any(tabuleiro[i][coluna] for i in range(len(tabuleiro))):
        return False

    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j]:
            return False

    for i, j in zip(range(linha, -1, -1), range(coluna, len(tabuleiro))):
        if tabuleiro[i][j]:
            return False

    return True

def nqueens(tabuleiro, linha):
    if linha == len(tabuleiro):
        return True

    for coluna in range(len(tabuleiro)):
        if verifica(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = 1

            if nqueens(tabuleiro, linha + 1):
                return True

            tabuleiro[linha][coluna] = 0

    return False

def main():
    arquivo = "input.gml"
    G = ler_input(arquivo)

    tabuleiro = [[0 for _ in range(8)] for _ in range(8)]

    if nqueens(tabuleiro, 0):
        print("Solução:")
        print_tabuleiro([linha.index(1) for linha in tabuleiro])
    else:
        print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()
