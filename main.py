#Programadores: Silas Leão, Lauro Stephan, João Vittor e Kauã Victor
from datetime import datetime
from ataque import *
from formarMatriz import *
from menu import *
from dados import *
import os


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

def mapearMatriz(tabuleiro):
    cont = 0
    for linha in range(1,ORDEM+1):
        for coluna in range(1,ORDEM+1):
            if tabuleiro[linha][coluna] == 'N ':
                cont+=1
    return cont


data = datetime.now()
dataformatada = (f'{data.day}-{data.month}-{data.hour}-{data.minute}')

if menu() == True:
    qtdeNavios = int(input('Informe a quantidade de navios que cada jogador terá(máx 6): '))
    if quantidadeNavios(qtdeNavios) == True:
        gerarTabuleiro(jogadorAGab,qtdeNavios)
        gerarTabuleiro(jogadorBGab,qtdeNavios)
        #Loop do jogo
        while True:
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
                    break
                elif contadorAcertosB == qtdeNavios:
                    print('Fim de jogo! Jogador B ganhou.')
                    break
                turno +=1
            else:
                arquivo = open(f'jogosalvos/jogo-{dataformatada}.txt','w')
                pasta = open('jogos-salvos.txt','a')
                pasta.write(f'jogo-{dataformatada}.txt'+'\n')
                salvarDados(arquivo,jogadorA,jogadorAGab,jogadorB,jogadorBGab)
                break
else:
    jogo_salvo = carregarJogo()
    realocarDados(jogo_salvo,jogadorA,jogadorAGab,jogadorB,jogadorBGab)
    qtdeNavios = mapearMatriz(jogadorAGab)
    while True:
            print(jogadorA)
            turno = contarTurnos(jogadorA)
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
                    break
                elif contadorAcertosB == qtdeNavios:
                    print('Fim de jogo! Jogador B ganhou.')
                    break
                turno +=1
            else:
                arquivo = open(f'jogosalvos/jogo-{dataformatada}.txt','w')
                pasta = open('jogos-salvos.txt','a')
                pasta.write(f'jogo-{dataformatada}.txt'+'\n')
                salvarDados(arquivo,jogadorA,jogadorAGab,jogadorB,jogadorBGab)
                break