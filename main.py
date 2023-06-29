#Programadores: Silas Leão, Lauro Stephan, João Vittor e Kauã Victor
from datetime import datetime
from ataque import *
from formarMatriz import *
from menu import *
import os

ORDEM = 8
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

data = datetime.now()
dataformatada = (f'{data.day}-{data.month}-{data.hour}-{data.minute}')
if menu() == True:
    qtdeNavios = int(input('Informe a quantidade de navios que cada jogador terá(máx 6): '))
    if quantidadeNavios(qtdeNavios) == True:
        gerarTabuleiro(jogadorAGab,qtdeNavios)
        gerarTabuleiro(jogadorBGab,qtdeNavios)
        #Loop do jogo
        turno = 1
        while fim != True:
            print(f'{turno}° TURNO.'+'\n')
            if salvarJogo() == True:
                print('Tabuleiro do jogador B:')
                mostrarTabuleiro(jogadorB)
                if atacarB(jogadorB, jogadorBGab) == True:
                    contadorAcertosA +=1
                print('Tabuleiro do jogador A:')
                mostrarTabuleiro(jogadorA)
                if atacarA(jogadorA, jogadorAGab) == True:
                    contadorAcertosB +=1
                if contadorAcertosA == qtdeNavios:
                    print('Fim de jogo! Jogador A ganhou.')
                    fim = True
                    break
                elif contadorAcertosB == qtdeNavios:
                    print('Fim de jogo! Jogador B ganhou.')
                    fim = True
                    break
                turno +=1
            else:
                arquivo = open(f'jogosalvos/jogo-{dataformatada}.txt','w')
                pasta = open('jogos-salvos.txt','a')
                pasta.write(f'jogo-{dataformatada}.txt'+'\n')
                for i in range(ORDEM+1):
                    for j in range(ORDEM+1):
                        arquivo.write(f'{jogadorA[i][j]}' + ' ')
                    arquivo.write('\n')
                for i in range(ORDEM+1):
                    for j in range(ORDEM+1):
                        arquivo.write(f'{jogadorAGab[i][j]}' + ' ')
                    arquivo.write('\n')
                for i in range(ORDEM+1):
                    for j in range(ORDEM+1):
                        arquivo.write(f'{jogadorB[i][j]}' + ' ')
                    arquivo.write('\n')
                for i in range(ORDEM+1):
                    for j in range(ORDEM+1):
                        arquivo.write(f'{jogadorBGab[i][j]}' + ' ')
                    arquivo.write('\n')
                break
else:
    print('deu merda')

