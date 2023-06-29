ORDEM = 8
COORDENADAS = ['','A |','B |','C |','D |','E |','F |','G |','H |']
contadorAcertosA = 0
contadorAcertosB = 0
fim = False
CoordenadaLinha = 0
CoordenadaColuna = 0

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

#Imprimir tabuleiro formatado
def mostrarTabuleiro(tabuleiro):
    for linha in range(ORDEM+1):
        for coluna in range(ORDEM+1):
            print(f'{tabuleiro[linha][coluna]:4}',end='')
        print('')


#Função para atacar o jogador A
def atacarA(tabuleiro, tabuleiroGab):
    global contadorAcertosB
    print('Vez do jogador B')
    coordenadasAtaque()
    if tabuleiroGab[CoordenadaLinha][CoordenadaColuna] == 'N':
        print('FOGO')
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'F'
        mostrarTabuleiro(tabuleiro) 
        print('Ataca novamente')   
        atacarA(tabuleiro, tabuleiroGab)
        return True
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
        print('Ataca novamente')
        atacarB(tabuleiro, tabuleiroGab)
        return True
    else:
        print('ÁGUA')
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'A'
        mostrarTabuleiro(tabuleiro) 
        print('Perde a vez')
