ORDEM = 8
def menu():
    global escolha
    escolha = int(input('''
    ESCOLHA UM OPÇÃO:\n
    1- NOVO JOGO
    2- CARREGAR JOGO\n
    : '''))
    
    if escolha < 1 or escolha >2:
        print('Escolha uma opção válida.')
        escolha = int(input('''
    ESCOLHA UM OPÇÃO:\n
    1- NOVO JOGO
    2- CARREGAR JOGO\n
    : '''))
    elif escolha == 1:
        return True
    else:
        return False

def salvarJogo():
    global salvar
    salvar = int(input('''
    1- CONTINUAR PARTIDA.
    2- SALVAR JOGO E SAIR.\n
    '''))
    if salvar == 1:
        return True
    else:
        return False

def carregarJogo():
    matriz = [[None]*(ORDEM+1) for linha in range(ORDEM+1)]
    file = open('jogos-salvos.txt','r')
    list = file.readlines()
    for k in range(len(list)):
        print(f'{k+1}° {list[k]}')
    escolha = int(input('Qual jogo será carregado? '))
    if escolha > len(list)+1 or escolha < 1:
        print('Escolha uma opção válida.')
    else:
        for k in range(len(list)):
            if escolha-1 == k:
                nome_arq = list[k].replace('\n','')
                jogo_carregado = open(f'jogosalvos/{nome_arq}', 'r')
        for i in range(9):
                matriz[i] = jogo_carregado.readlines(i)
    print(matriz)
carregarJogo()