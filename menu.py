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
        