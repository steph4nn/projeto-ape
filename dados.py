def salvarDados(arquivo,jogadorA, jogadorAGab, jogadorB, jogadorBGab):
    ORDEM = 8
    for i in range(1,ORDEM+1):
        for j in range(1,ORDEM+1):
            arquivo.write(f'{jogadorA[i][j]}' + ' ')
            arquivo.write('\n')
    for i in range(1,ORDEM+1):
        for j in range(1,ORDEM+1):
            arquivo.write(f'{jogadorAGab[i][j]}' + ' ')
            arquivo.write('\n')
    for i in range(1,ORDEM+1):
        for j in range(1,ORDEM+1):
            arquivo.write(f'{jogadorB[i][j]}' + ' ')
            arquivo.write('\n')
    for i in range(1,ORDEM+1):
        for j in range(1,ORDEM+1):
            arquivo.write(f'{jogadorBGab[i][j]}' + ' ')
            arquivo.write('\n')


def realocarDados(arquivo,jogadorA, jogadorAGab, jogadorB, jogadorBGab):
    
    vetores_formatados = []
    linha = []
    #reaolocando os dados do JogadorA
    for i in range(64):
        linha.append(arquivo[i].replace('\n',''))
        if len(linha) == 8:
            vetores_formatados.append(linha)
            linha= []
    for i in range(8):
        for j in range(8):
            if i == 0 and j==0:
                jogadorA[i][j] = ''    
            jogadorA[i+1][j+1] = vetores_formatados[i][j]

    #reacolando os dados do JogadorAGab
    vetores_formatados = []
    linha = []

    for i in range(64,128):
        linha.append(arquivo[i].replace('\n',''))
        if len(linha) == 8:
            vetores_formatados.append(linha)
            linha= []
    for i in range(8):
        for j in range(8):
            if i == 0 and j==0:
                jogadorAGab[i][j] = ''    
            jogadorAGab[i+1][j+1] = vetores_formatados[i][j]
    
    #realocando os doados do jogadorB
    vetores_formatados = []
    linha = []

    for i in range(128,192):
        linha.append(arquivo[i].replace('\n',''))
        if len(linha) == 8:
            vetores_formatados.append(linha)
            linha= []
    for i in range(8):
        for j in range(8):
            if i == 0 and j==0:
                jogadorB[i][j] = ''    
            jogadorB[i+1][j+1] = vetores_formatados[i][j]

    #realocando os dados do jogadorBgab
    vetores_formatados = []
    linha = []

    for i in range(192,256):
        linha.append(arquivo[i].replace('\n',''))
        if len(linha) == 8:
            vetores_formatados.append(linha)
            linha= []
    for i in range(8):
        for j in range(8):
            if i == 0 and j==0:
                jogadorBGab[i][j] = ''    
            jogadorBGab[i+1][j+1] = vetores_formatados[i][j]