#Programadores: Silas Leão, Lauro Stephan, João Vittor e Kauã Victor
from ataque import *
from formarMatriz import *
from menu import *

ORDEM = 8
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


if menu() == True:
    quantidadeNavios()
    gerarTabuleiro(jogadorAGab)
    gerarTabuleiro(jogadorBGab)

#Loop do jogo
turno = 1
while fim != True:
    print(f'{turno}° TURNO.'+'\n')
    if escolha == True:
        print('Tabuleiro do jogador B:')
        mostrarTabuleiro(jogadorB)
        atacarB(jogadorB, jogadorBGab)
        print('Tabuleiro do jogador A:')
        mostrarTabuleiro(jogadorA)
        atacarA(jogadorA, jogadorAGab)
        if contadorAcertosA == qtdeNavios:
            print('Fim de jogo! Jogador A ganhou.')
            fim = True
            break
        elif contadorAcertosB == qtdeNavios:
            print('Fim de jogo! Jogador B ganhou.')
            fim = True
            break

