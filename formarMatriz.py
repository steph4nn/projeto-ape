ORDEM = 8
LETRAS = ['A','N','A','A','A']
import random

#Definição da quantidade de navios para os jogadores
def quantidadeNavios(qtdeNavios):
    if qtdeNavios > 6:
        print('Quantidade de navios não pode exceder 6')
    elif qtdeNavios <1:
        print('Quantidade de navios não pode ser igual ou menor que 0')
    else:
        return True

#Mapear o tabuleiro para saber a quantidade de navios já existentes
def mapearMatriz(tabuleiro):
    result = 0
    for linha in range(ORDEM+1):
        for coluna in range(ORDEM+1):
            if tabuleiro[linha][coluna] == 'N':
                result+=1
    return result

#Função para verificar se há espaço disponível para navios(horizontal e vertical)
def verificarLados(tabuleiro, linha, coluna):
    if coluna+1 < ORDEM+1 and tabuleiro[linha][coluna+1] == 'N':
        return False
    elif linha+1<ORDEM+1 and tabuleiro[linha+1][coluna] == 'N':
        return False
    elif linha-1 >= 0 and tabuleiro[linha-1][coluna] == 'N':
        return False
    elif coluna-1 >= 0 and tabuleiro[linha][coluna-1] == 'N':
        return False
    else:
        return True

#Função para verificar se há espaço disponível para navios(diagonais)
def verificarDiagonais(tabuleiro, linha, coluna):
    if linha-1>=0 and coluna-1>=0 and tabuleiro[linha-1][coluna-1] == 'N':
        return False
    elif linha+1<ORDEM+1 and coluna+1<ORDEM+1 and tabuleiro[linha+1][coluna+1] == 'N':
        return False
    elif linha+1<ORDEM+1 and coluna-1>=0 and tabuleiro[linha+1][coluna-1] == 'N':
        return False
    elif linha-1>=0 and coluna+1<ORDEM+1 and tabuleiro[linha-1][coluna+1] =='N':
        return False
    else:
        return True

#Preenchimento da matriz com células N(navio) e A(água/espaço vazio)
def gerarTabuleiro(tabuleiro, qtdeNavios):
    cont_i=1
    cont_j=1
    for linha in range(1, ORDEM+1):
        for coluna in range(1, ORDEM+1):
            if mapearMatriz(tabuleiro) < qtdeNavios:
                if verificarLados(tabuleiro, cont_i, cont_j) == True and verificarDiagonais(tabuleiro, cont_i, cont_j):
                    tabuleiro[linha][coluna] = random.choice(LETRAS)
                else:
                    tabuleiro[linha][coluna] = 'A'
            else:
                tabuleiro[linha][coluna] = 'A'
            cont_j+=1
        cont_j = 1    
        cont_i+=1
    return tabuleiro

#função para retornar a quantidade de navios
<<<<<<< HEAD
=======
def mapearMatriz(tabuleiro):
    cont = 0
    for linha in range(1,ORDEM+1):
        for coluna in range(1,ORDEM+1):
            if tabuleiro[linha][coluna] == 'N ':
                cont+=1
    return cont
>>>>>>> 13c626712cd88caa4c6fbaba6d78bade30b06493

#função para retornar a quantidade de turnos jogados
def contarTurnos(tabuleiro):
    cont = 0
    for linha in range(1,ORDEM+1):
        for coluna in range(1,ORDEM+1):
            if tabuleiro[linha][coluna] == 'A ':
                cont+=1
            if tabuleiro[linha][coluna] == 'F ':
                cont-=1
    return cont