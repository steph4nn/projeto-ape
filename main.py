import random
ORDEM = 8
LETRAS = ['A','N']


jogadorA = [[0]*ORDEM for linha in range(ORDEM)]


def mapearMatriz(tabuleiro):
    result = 0
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            if tabuleiro[linha][coluna] == 'N':
                result+=1
    return result

def verificarLados(tabuleiro):
    result = True
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            if coluna+1 < ORDEM and tabuleiro[linha][coluna+1] == 'N':
                result = False
            elif linha+1<ORDEM and tabuleiro[linha+1][coluna] == 'N':
                result = False
            elif linha-1 >= 0 and tabuleiro[linha-1][coluna] == 'N':
                result = False
            elif coluna-1 >= 0 and tabuleiro[linha][coluna-1] == 'N':
                result = False
    return result

def gerarTabuleiro(tabuleiro):
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            if mapearMatriz(tabuleiro) < 6:
                if verificarLados(tabuleiro) == True:
                    tabuleiro[linha][coluna] = random.choice(LETRAS)
                else:
                    tabuleiro[linha][coluna] = 'A'
    return tabuleiro

def mostrarTabuleiro(tabuleiro):
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            print(f'{tabuleiro[linha][coluna]:4}',end='')
        print('')



gerarTabuleiro(jogadorA)
mostrarTabuleiro(jogadorA)