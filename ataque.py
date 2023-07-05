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
        case _:
            print('Coordenada inválida, tente novamente!')
            coordenadasAtaque()

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
        case _:
            print('Coordenada inválida, tente novamente!')
            coordenadasAtaque()

#Imprimir tabuleiro formatado
def mostrarTabuleiro(tabuleiro):
    for linha in range(ORDEM+1):
        for coluna in range(ORDEM+1):
            print(f'{tabuleiro[linha][coluna]:4}',end='')
        print('')


#Função para atacar o jogador A
def atacarA(tabuleiro, tabuleiroGab):
    global contadorAcertosB
    print()
    print('Vez do jogador B')
    print()
    coordenadasAtaque()
    if tabuleiroGab[CoordenadaLinha][CoordenadaColuna] == 'N':
        print()
        print('\033[1;33;41m FOGO \033[m')
        print()
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'F'
        mostrarTabuleiro(tabuleiro) 
        print()
        print('\033[1;32m Você acertou!! Ataque novamente.\033[m')  
        atacarA(tabuleiro, tabuleiroGab)
        return True
    else:
        print()
        print('\033[1;36;44m ÁGUA \033[m')
        print()
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'A'
        mostrarTabuleiro(tabuleiro) 
        print()
        print('\033[1;31mPerdeu sua vez\033[m')
        print()

#Função para atacar o jogador B
def atacarB(tabuleiro, tabuleiroGab):
    global contadorAcertosA
    print()
    print('Vez do jogador A')
    print()
    coordenadasAtaque()
    if tabuleiroGab[CoordenadaLinha][CoordenadaColuna] == 'N':
        print()
        print('\033[1;33;41m FOGO \033[m')
        print()
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'F'
        mostrarTabuleiro(tabuleiro) 
        print()
        print('\033[1;32mVocê acertou!! Ataque novamente.\033[m')
        atacarB(tabuleiro, tabuleiroGab)
        return True
    else:
        print()
        print('\033[1;36;44m ÁGUA \033[m')
        print()
        tabuleiro[CoordenadaLinha][CoordenadaColuna] = 'A'
        mostrarTabuleiro(tabuleiro) 
        print()
        print('\033[1;31mPerdeu sua vez\033[m')
        
