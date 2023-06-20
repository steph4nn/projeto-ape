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

def verificarLados(tabuleiro, linha, coluna):

            if coluna+1 < ORDEM and tabuleiro[linha][coluna+1] == 'N':
                return False
            elif linha+1<ORDEM and tabuleiro[linha+1][coluna] == 'N':
                return False
            elif linha-1 >= 0 and tabuleiro[linha-1][coluna] == 'N':
                return False
            elif coluna-1 >= 0 and tabuleiro[linha][coluna-1] == 'N':
                return False
            else:
                return True

def gerarTabuleiro(tabuleiro):
    cont_i=0
    cont_j=0
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            if mapearMatriz(tabuleiro) <= 6:
                if verificarLados(tabuleiro, cont_i, cont_j) == True:
                    tabuleiro[linha][coluna] = random.choice(LETRAS)
                else:
                    tabuleiro[linha][coluna] = 'A'
            else:
                tabuleiro[linha][coluna] = 'A'
            cont_j+=1
        cont_j = 0    
        cont_i+=1
    return tabuleiro

def mostrarTabuleiro(tabuleiro):
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            print(f'{tabuleiro[linha][coluna]:4}',end='')
        print('')


gerarTabuleiro(jogadorA)
mostrarTabuleiro(jogadorA)