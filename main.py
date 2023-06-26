import random
ORDEM = 8
LETRAS = ['A','N','A','A','A']
qtdeNavios = 0
COORDENADAS = [None,'A','B','C','D','E','F','G','H']
#Criação do tabuleiro do primeiro jogador
jogadorA = [[None]*(ORDEM+1) for linha in range(ORDEM+1)]

#Coordenadas do tabuleiro
for i in range(ORDEM+1):
    for j in range(1, ORDEM+1):
        jogadorA[i][j] = COORDENADAS[j]
    break
for k in range(ORDEM+1):
    for t in range(1, ORDEM+1):
        jogadorA[t][k] = COORDENADAS[t]
    break
    
#Definição da quantidade de navios para os jogadores
def quantidadeNavios():
    global qtdeNavios
    qtdeNavios = int(input('Informe a quantidade de navios que cada jogador terá(máx 6): '))
    if qtdeNavios > 6:
        print('Quantidade de navios não pode exceder 6')
        qtdeNavios = int(input('Informe a quantidade de navios que cada jogador terá(máx 6): '))
    elif qtdeNavios <= 0:
        print('Quantidade de navios não pode ser igual ou menor que 0')
        qtdeNavios = int(input('Informe a quantidade de navios que cada jogador terá(máx 6): '))
    return qtdeNavios
quantidadeNavios()

#Mapear o tabuleiro para saber a quantidade de navios já existentes
def mapearMatriz(tabuleiro):
    result = 0
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            if tabuleiro[linha][coluna] == 'N':
                result+=1
    return result

#Função para verificar se há espaço disponível para navios(horizontal e vertical)
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

#Função para verificar se há espaço disponível para navios(diagonais)
def verificarDiagonais(tabuleiro, linha, coluna):
    if linha-1>=0 and coluna-1>=0 and tabuleiro[linha-1][coluna-1] == 'N':
        return False
    elif linha+1<ORDEM and coluna+1<ORDEM and tabuleiro[linha+1][coluna+1] == 'N':
        return False
    elif linha+1<ORDEM and coluna-1>=0 and tabuleiro[linha+1][coluna-1] == 'N':
        return False
    elif linha-1>=0 and coluna+1<ORDEM and tabuleiro[linha-1][coluna+1] =='N':
        return False
    else:
        return True

#Preenchimento da matriz com células N(navio) e A(água/espaço vazio)
def gerarTabuleiro(tabuleiro):
    cont_i=0
    cont_j=0
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            if mapearMatriz(tabuleiro) < qtdeNavios:
                if verificarLados(tabuleiro, cont_i, cont_j) == True and verificarDiagonais(tabuleiro, cont_i, cont_j):
                    tabuleiro[linha][coluna] = random.choice(LETRAS)
                else:
                    tabuleiro[linha][coluna] = 'A'
            else:
                tabuleiro[linha][coluna] = 'A'
            cont_j+=1
        cont_j = 0    
        cont_i+=1
    return tabuleiro

#Imprimir tabuleiro formatado
def mostrarTabuleiro(tabuleiro):
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            print(f'{tabuleiro[linha][coluna]:4}',end='')
        print('')

gerarTabuleiro(jogadorA)
mostrarTabuleiro(jogadorA)