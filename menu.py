ORDEM = 8


def menu():
    global escolha
    print()
    print('\033[1;34;40mVAMOS\033[m \033[1;31;40mJOGAR\033[m \033[1;34;40mBATALHA\033[m \033[1;31;40mNAVAL\033[m \033[1;34;40m!\033[m\033[1;31;40m!\033[m\033[1;34;40m!\033[m\033[1;31;40m!\033[m\033[1;34;40m!\033[m')
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
    elif salvar == 9:
        return 9
    elif salvar == 2:
        return False

def carregarJogo():
    file = open('jogos-salvos.txt','r')
    list = file.readlines()
    for k in range(len(list)):
        print(f'{k+1}° {list[k]}')
    escolha = int(input('Qual jogo será carregado? '))
    while escolha > len(list)+1 or escolha < 1:
        escolha = int(input('Escolha um arquivo válido. Qual jogo será carregado? '))
    for k in range(len(list)):
            if escolha-1 == k:
                nome_arq = list[k].replace('\n','')
                jogo_carregado = open(f'jogosalvos/{nome_arq}', 'r')
                vetores = jogo_carregado.readlines()
                return vetores
    