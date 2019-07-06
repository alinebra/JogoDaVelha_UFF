import random as rd


def MostraTabuleiro(t):
    print(' ' + t[0][0] + ' |  ' + t[0][1] + '  |  ' + t[0][2])
    print('-----------------')
    print('  ' + t[1][0] + ' |  ' + t[1][1] + '  |  ' + t[1][2])
    print('-----------------')
    print('  ' + t[2][0] + ' |  ' + t[2][1] + '  |  ' + t[2][2])


def JogadaBot01(t, marca):
    # joga no centro:
    if t[1][1] == '':
        jogada = str(1) + ',' + str(1)
        return jogada
    # joga nos cantos
    elif t[0][0] == '':
        jogada = str(0) + ',' + str(0)
        return jogada
    elif t[2][2] == '':
        jogada = str(2) + ',' + str(2)
        return jogada
    elif t[0][2] == '':
        jogada = str(0) + ',' + str(2)
        return jogada
    elif t[2][0] == '':
        jogada = str(2) + ',' + str(0)
        return jogada


def ChecaVitoria(t, m):
    if ((t[0][0] == m and t[0][1] == m and t[0][2] == m) or  # primeira linha
            (t[1][0] == m and t[1][1] == m and t[1][2] == m) or  # segunda linha
            (t[2][0] == m and t[2][1] == m and t[2][2] == m) or  # terceira linha
            (t[0][0] == m and t[1][0] == m and t[2][0] == m) or  # primeira coluna
            (t[0][1] == m and t[1][1] == m and t[2][1] == m) or  # segunda coluna
            (t[0][2] == m and t[1][2] == m and t[2][2] == m) or  # terceira coluna
            (t[0][0] == m and t[1][1] == m and t[2][2] == m) or  # diagonal principal
            (t[2][0] == m and t[1][1] == m and t[0][2] == m)):  # diagonal secundaria
        return True
    else:
        return False


def ChecaEmpate(t):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if t[i][j] != '':
                count += 1
    return count


def CopiaTabuleiro(t):
    Falso = t.copy()
    return Falso


def MelhorJogada(f, mark):
    loop = True
    while loop == True:
        f2 = f.copy()
        for i in range(0, 3):
            for j in range(0, 3):
                if f2[i][j] == '':
                    f2[i][j] = mark
                    if ChecaVitoria(f2, mark) == True:
                        loop = False
                        temp = str(i) + ',' + str(j)
                        f2[i][j] = ''
                        return temp
                    f2[i][j] = ''
        loop = False


def JogadaBot2(t, marca):
    Fake = CopiaTabuleiro(t)
    if marca == 'X':
        if rodada == 1:
            if MelhorJogada(Fake, '0'):
                # se o humano nao ganhar vai jogar random na segunda rodada
                teste = MelhorJogada(Fake, '0')
                i = int(teste.split(',')[0])
                j = int(teste.split(',')[1])
                jogada = str(i) + ',' + str(j)

            else:
                i = rd.randint(0, 2)
                j = rd.randint(0, 2)
                while t[i][j] != '':
                    i = rd.randint(0, 2)
                    j = rd.randint(0, 2)
                jogada = str(i) + ',' + str(j)

        else:
            # se nao for a segunda rodada, vai tentar ganhar primeiro
            if MelhorJogada(Fake, marca):
                jogada = MelhorJogada(Fake, marca)
            elif MelhorJogada(Fake, '0'):
                teste = MelhorJogada(Fake, '0')
                i = int(teste.split(',')[0])
                j = int(teste.split(',')[1])
                jogada = str(i) + ',' + str(j)
            else:
                # se o humano nao ganhar vai jogar random
                i = rd.randint(0, 2)
                j = rd.randint(0, 2)
                while t[i][j] != '':
                    i = rd.randint(0, 2)
                    j = rd.randint(0, 2)
                jogada = str(i) + ',' + str(j)
    else:
        # se nao for a segunda rodada, vai tentar ganhar primeiro
        if MelhorJogada(Fake, marca):
            jogada = MelhorJogada(Fake, marca)
        elif MelhorJogada(Fake, 'X'):
            teste = MelhorJogada(Fake, 'X')
            i = int(teste.split(',')[0])
            j = int(teste.split(',')[1])
            jogada = str(i) + ',' + str(j)
        else:
            # se o humano nao ganhar vai jogar random
            i = rd.randint(0, 2)
            j = rd.randint(0, 2)
            while t[i][j] != '':
                i = rd.randint(0, 2)
                j = rd.randint(0, 2)
            jogada = str(i) + ',' + str(j)
    return jogada


dic = {
    1: '0,0',
    2: '0,1',
    3: '0,2',
    4: '1,0',
    5: '1,1',
    6: '1,2',
    7: '2,0',
    8: '2,1',
    9: '2,2'
}

Jogando = True
while Jogando:
    Jogo = True
    rodada = 0
    Tabuleiro = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]
    print('Você quer ser o primeiro ou o segundo? (1/2)')
    if input() == '1':
        MarcaHumano = '0'
        MarcaBot = 'X'
    else:
        MarcaHumano = 'X'
        MarcaBot = '0'
    print('Sua marca é: ' + MarcaHumano)
    print('    ' + '1' + ' |  ' + '2' + '  |  ' + '3')
    print('-----------------')
    print('    ' + '4' + ' |  ' + '5' + '  |  ' + '6')
    print('-----------------')
    print('    ' + '7' + ' |  ' + '8' + '  |  ' + '9')
    while Jogo:
        if MarcaHumano == '0':
            # vez humano:
            opcao = input('Sua vez, diga o local: (1 ~ 9)')
            local = dic[int(opcao)]
            linha = int(local.split(',')[0])
            coluna = int(local.split(',')[1])
            while Tabuleiro[linha][coluna] != '':
                print('Já tem uma marca nesse local!')
                opcao = input('Sua vez, diga o local: (1 ~ 9)')
                local = dic[int(opcao)]
                linha = int(local.split(',')[0])
                coluna = int(local.split(',')[1])
            Tabuleiro[linha][coluna] = MarcaHumano
            MostraTabuleiro(Tabuleiro)
            print('\n###############\n')
            if ChecaEmpate(Tabuleiro) == 9:
                print('Empatou!')
                Jogo = False
                continue
            if ChecaVitoria(Tabuleiro, MarcaHumano):
                print('Você ganhou! :D')
                Jogo = False
                continue
            # vez bot:
            if rodada < 1:
                local = JogadaBot01(Tabuleiro, MarcaBot)
            else:
                local = JogadaBot2(Tabuleiro, MarcaBot)
            linha = int(local.split(',')[0])
            coluna = int(local.split(',')[1])
            Tabuleiro[linha][coluna] = MarcaBot
            MostraTabuleiro(Tabuleiro)
            print('\n###############\n')
            if ChecaEmpate(Tabuleiro) == 9:
                print('Empatou!')
                Jogo = False
                continue
            if ChecaVitoria(Tabuleiro, MarcaBot):
                print('Eu ganhei! :D')
                Jogo = False
                continue
        else:
            # vez bot
            if rodada < 2:
                local = JogadaBot01(Tabuleiro, MarcaBot)
            else:
                local = JogadaBot2(Tabuleiro, MarcaBot)
            linha = int(local.split(',')[0])
            coluna = int(local.split(',')[1])
            Tabuleiro[linha][coluna] = MarcaBot
            MostraTabuleiro(Tabuleiro)
            print('\n###############\n')
            if ChecaEmpate(Tabuleiro) == 9:
                print('Empatou!')
                Jogo = False
                continue
            if ChecaVitoria(Tabuleiro, MarcaBot):
                print('Eu ganhei! :D')
                Jogo = False
                continue
            # vez humano
            opcao = input('Sua vez, diga o local: (1 ~ 9)')
            local = dic[int(opcao)]
            linha = int(local.split(',')[0])
            coluna = int(local.split(',')[1])

            while Tabuleiro[linha][coluna] != '':
                print('Já tem uma marca nesse local!')
                opcao = input('Sua vez, diga o local: (1 ~ 9)')
                local = dic[int(opcao)]
                linha = int(local.split(',')[0])
                coluna = int(local.split(',')[1])
            Tabuleiro[linha][coluna] = MarcaHumano
            MostraTabuleiro(Tabuleiro)
            print('\n###############\n')
            if ChecaEmpate(Tabuleiro) == 9:
                print('Empatou!')
                Jogo = False
                continue
            if ChecaVitoria(Tabuleiro, MarcaHumano):
                print('Você ganhou! :D')
                Jogo = False
                continue
        rodada += 1
    print('Continuar jogando? (S/N)')
    inp = input()
    if inp != 's' and inp != 'S':
        Jogando = False
