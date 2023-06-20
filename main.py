import random
ORDEM = 8
LETRAS = ['A','N']


jogadorA = [[0]*ORDEM for linha in range(ORDEM)]



def gerarTabuleiro(tabuleiro):
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
                tabuleiro[linha][coluna] = random.choice(LETRAS)
    return tabuleiro



def mostrarTabuleiro(tabuleiro):
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            print(f'{tabuleiro[linha][coluna]:4}',end='')
        print('')



gerarTabuleiro(jogadorA)
mostrarTabuleiro(jogadorA)