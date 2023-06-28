#Programadores: Silas Leão, Lauro Stephan, João Vittor e Kauã Victor

import random
ORDEM = 8
LETRAS = ['A','N','A','A','A']
qtdeNavios = 0
COORDENADAS = ['','A |','B |','C |','D |','E |','F |','G |','H |']
contadorAcertosA = 0
contadorAcertosB = 0
fim = False
CoordenadaLinha = 0
CoordenadaColuna = 0

#Criação dos tabuleiros gabarito
jogadorAGab = [[None]*(ORDEM+1) for linha in range(ORDEM+1)]
jogadorBGab = [[None]*(ORDEM+1) for linha in range(ORDEM+1)]

#Criação dos tabuleiros vazios para a partida
jogadorA = [[' ']*(ORDEM+1) for linha in range(ORDEM+1)]
jogadorB = [[' ']*(ORDEM+1) for linha in range(ORDEM+1)]

#Coordenadas do tabuleiro gabarito A
for linha in range(ORDEM+1):
    jogadorAGab[0][linha] = COORDENADAS[linha]
    jogadorAGab[linha][0] = COORDENADAS[linha]
#Coordenadas do tabuleiro gabarito B
for linha in range(ORDEM+1):
    jogadorBGab[0][linha] = COORDENADAS[linha]
    jogadorBGab[linha][0] = COORDENADAS[linha]

#Coordenadas do tabuleiro A vazio
for linha in range(ORDEM+1):
    jogadorA[0][linha] = COORDENADAS[linha]
    jogadorA[linha][0] = COORDENADAS[linha]
#Coordenadas do tabuleiro B vazio
for linha in range(ORDEM+1):
    jogadorB[0][linha] = COORDENADAS[linha]
    jogadorB[linha][0] = COORDENADAS[linha]

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
def gerarTabuleiro(tabuleiro):
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

#Imprimir tabuleiro formatado
def mostrarTabuleiro(tabuleiro):
    for linha in range(ORDEM+1):
        for coluna in range(ORDEM+1):
            print(f'{tabuleiro[linha][coluna]:4}',end='')
        print('')

#Função para coletar as coordenadas do ataque
def coordenadasAtaque():
    global CoordenadaLinha, CoordenadaColuna
    CoordenadaLinha = input('Informe a coordenada linha do seu ataque(A-H): ').upper()
    CoordenadaColuna = input('Informe a coordenada coluna do seu ataque(A-H): ').upper()
    match CoordenadaLinha:
        case 'A':
            CoordenadaLinha = 1
        case 'B':
            CoordenadaLinha = 2
        case 'C':
            CoordenadaLinha = 3
        case 'D':
            CoordenadaLinha = 4
        case 'E':
            CoordenadaLinha = 5
        case 'F':
            CoordenadaLinha = 6
        case 'G':
            CoordenadaLinha = 7
        case 'H':
            CoordenadaLinha = 8

    match CoordenadaColuna:
        case 'A':
            CoordenadaColuna = 1
        case 'B':
            CoordenadaColuna = 2
        case 'C':
            CoordenadaColuna = 3
        case 'D':
            CoordenadaColuna = 4
        case 'E':
            CoordenadaColuna = 5
        case 'F':
            CoordenadaColuna = 6
        case 'G':
            CoordenadaColuna = 7
        case 'H':
            CoordenadaColuna = 8

#Função para atacar o jogador A
def atacarA(tabuleiro, tabuleiroGab):
    global contadorAcertosB
    print('Vez do jogador B')
    coordenadasAtaque()
    if tabuleiroGab[CoordenadaLinha][CoordenadaColuna] == 'N':
        print('FOGO')
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'F'
        mostrarTabuleiro(tabuleiro) 
        contadorAcertosB += 1
        print('Ataca novamente')   
        atacarA(tabuleiro, tabuleiroGab)
    else:
        print('ÁGUA')
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'A'
        mostrarTabuleiro(tabuleiro) 
        print('Perde a vez')

#Função para atacar o jogador B
def atacarB(tabuleiro, tabuleiroGab):
    global contadorAcertosA
    print('Vez do jogador A')
    coordenadasAtaque()
    if tabuleiroGab[CoordenadaLinha][CoordenadaColuna] == 'N':
        print('FOGO')
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'F'
        mostrarTabuleiro(tabuleiro) 
        contadorAcertosA += 1
        print('Ataca novamente')
        atacarB(tabuleiro, tabuleiroGab)
    else:
        print('ÁGUA')
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'A'
        mostrarTabuleiro(tabuleiro) 
        print('Perde a vez')

gerarTabuleiro(jogadorAGab)
gerarTabuleiro(jogadorBGab)

#Loop do jogo
while fim != True:
    print('Tabuleiro do jogador A:')
    mostrarTabuleiro(jogadorA)
    print('Tabuleiro do jogador B:')
    mostrarTabuleiro(jogadorB)
    atacarB(jogadorB, jogadorBGab)
    atacarA(jogadorA, jogadorAGab)
    if contadorAcertosA == qtdeNavios:
        print('Fim de jogo! Jogador A ganhou.')
        fim = True
        break
    elif contadorAcertosB == qtdeNavios:
        print('Fim de jogo! Jogador B ganhou.')
        fim = True
        break
