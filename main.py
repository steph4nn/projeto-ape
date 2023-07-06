#Programadores: Silas Leão, Lauro Stephan, João Vittor e Kauã Victor
from datetime import datetime
from ataque import *
from formarMatriz import *
from menu import *
from dados import *
import os

sdsdsdsdsddsdsd
ORDEM = 8
COORDENADAS = ['','A |','B |','C |','D |','E |','F |','G |','H |']

contadorAcertosA = 0
contadorAcertosB = 0
turno = 1
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
    print()
    qtdeNavios = int(input('\033[1;33mInforme a quantidade de navios que cada jogador terá(máx 6): \033[m'))
    print()
    if quantidadeNavios(qtdeNavios) == True:
        gerarTabuleiro(jogadorAGab,qtdeNavios)
        gerarTabuleiro(jogadorBGab,qtdeNavios)
        #Loop do jogo
        while True:
            print()
            print(f'{turno}° TURNO.'+'\n')
            resp = salvarJogo()
            if resp == True:
                print()
                print('Tabuleiro do jogador B:\n')
                mostrarTabuleiro(jogadorB)
                if atacarB(jogadorB, jogadorBGab) == True:
                    contadorAcertosA +=1
                print()
                print('Tabuleiro do jogador A:\n')
                mostrarTabuleiro(jogadorA)
                if atacarA(jogadorA, jogadorAGab) == True:
                    contadorAcertosB +=1
                if contadorAcertosA == qtdeNavios:
                    print('\033[1;32mFim de jogo! Jogador A ganhou.\033[m')
                    break
                elif contadorAcertosB == qtdeNavios:
                    print('\033[1;32mFim de jogo! Jogador B ganhou.\033[m')
                    break
                turno +=1
            elif resp == False:
                arquivo = open(f'jogosalvos/jogo-{dataformatada}.txt','w')
                pasta = open('jogos-salvos.txt','a')
                pasta.write(f'jogo-{dataformatada}.txt'+'\n')
                salvarDados(arquivo,jogadorA,jogadorAGab,jogadorB,jogadorBGab)
                break
            elif resp == 9:
                print(f'Gabarito do jogador A\n')
                mostrarTabuleiro(jogadorAGab)
                print()
                print('Gabarito do jogador B\n')
                mostrarTabuleiro(jogadorBGab)
            else:
                print('Digite uma opção válida, tente novamente.')
                salvarJogo()
else:
    jogo_salvo = carregarJogo()
    realocarDados(jogo_salvo,jogadorA,jogadorAGab,jogadorB,jogadorBGab)
    qtdeNavios = mapearMatriz(jogadorAGab)
    while True:
            turno = contarTurnos(jogadorA)
            print(f'{turno}° TURNO.'+'\n')
            resp = salvarJogo()
            if resp == True:
                print()
                print('Tabuleiro do jogador B:\n')
                mostrarTabuleiro(jogadorB)
                if atacarB(jogadorB, jogadorBGab) == True:
                    contadorAcertosA +=1
                print()
                print('Tabuleiro do jogador A:\n')
                mostrarTabuleiro(jogadorA)
                if atacarA(jogadorA, jogadorAGab) == True:
                    contadorAcertosB +=1
                if contadorAcertosA == qtdeNavios:
                    print('\033[1;32mFim de jogo! Jogador A ganhou.\033[m')
                    break
                elif contadorAcertosB == qtdeNavios:
                    print('\033[1;32mFim de jogo! Jogador B ganhou.\033[m')
                    break
                turno +=1
            elif resp == False:
                arquivo = open(f'jogosalvos/jogo-{dataformatada}.txt','w')
                pasta = open('jogos-salvos.txt','a')
                pasta.write(f'jogo-{dataformatada}.txt'+'\n')
                salvarDados(arquivo,jogadorA,jogadorAGab,jogadorB,jogadorBGab)
                break
            elif resp == 9:
                print(f'Gabarito do jogador A\n')
                mostrarTabuleiro(jogadorAGab)
                print()
                print('Gabarito do jogador B\n')
                mostrarTabuleiro(jogadorBGab)