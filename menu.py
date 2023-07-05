ORDEM = 8

#Função do menu, oferecendo todas as funções do programa
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
    