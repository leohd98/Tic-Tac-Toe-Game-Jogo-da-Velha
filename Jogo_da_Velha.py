#- Player 1 decides between [X] or [O] picto/symbol -----------------
while True:
     jogador1 = str(input('Player 1, deseja ser [X] ou [O]?: ')).upper()
     if jogador1 != 'X' and jogador1 != 'O':
          print()
          print('ERRO, ESCOLHA APENAS OPÇÕES VÁLIDAS [X OU O]')
          print()
     else:
          break
jogador2 = ''
if jogador1 == 'X':
    jogador2 = 'O'
else:
    jogador2 = 'X'
#---------------------------------------

#- It draws the board in its initial state ----------
linha1 = list('  7 | 8 | 9 ')
linha_layout1 = list(' ---+---+---')
linha2 = list('  4 | 5 | 6 ')
linha_layout2 = list(' ---+---+---')
linha3 = list('  1 | 2 | 3 ')
#---------------------------------------

#- Shows and update the board while the game is being played -------
vitorioso = 0
escolha1 = ''
escolha2 = ''
escolhas_player1 = []
escolhas_player2 = []
y = 0
while True:
    for x in range(100):
         print()
    print('JOGO DA VELHA')
    print('=============\n ')
    print(''.join(linha1))
    print(''.join(linha_layout1))
    print(''.join(linha2))
    print(''.join(linha_layout2))
    print(''.join(linha3))
    print()
    print(f"Player 1: [{jogador1}]")
    print(f"Player 2: [{jogador2}]")
    print()
    if escolha1 in escolhas_player2 or escolha2 in escolhas_player1:
            print('[!ERRO!] O OUTRO JOGADOR JÁ ESCOLHEU ESTE NÚMERO [!ERRO!]')
    elif vitorioso == 1:
         print(f'PARABÉNS, JOGADOR 1[{jogador1}] É VITORIOSO!')
         break
    elif vitorioso == 2:
         print(f'PARABÉNS, JOGADOR 2[{jogador2}] É VITORIOSO!')
         break
#---------------------------------------
    
    #Player 2 -------------------------
    if y == 1:
        escolha2 = str(input('[Player 2]\nEscolha a posição: '))
        if escolha2 in escolhas_player1:
            continue
        elif escolha2 in linha1:
            x = linha1.index(escolha2)
            linha1[x] = jogador2
            x = 0
            y = 0
        elif escolha2 in linha2:
            x = linha2.index(escolha2)
            linha2[x] = jogador2
            x = 0
            y = 0
        elif escolha2 in linha3:
            x = linha3.index(escolha2)
            linha3[x] = jogador2
            x = 0
            y = 0
        escolhas_player2 += escolha2
        continue
    #-----------------------------------

    #Player 1 -------------------------
    escolha1 = str(input('[Player 1]\nEscolha a posição: '))
    if escolha1 in escolhas_player2:
            continue
    if escolha1 in linha1:
        x = linha1.index(escolha1)
        linha1[x] = jogador1
        x = 0
        y += 1
    elif escolha1 in linha2:
        x = linha2.index(escolha1)
        linha2[x] = jogador1
        x = 0
        y += 1
    elif escolha1 in linha3:
        x = linha3.index(escolha1)
        linha3[x] = jogador1
        x = 0
        y += 1
    escolhas_player1 += escolha1
    #-----------------------------------

    # All win possibilities:
    if all(numeros in escolhas_player1 for numeros in ['7', '5', '3']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['7', '5', '3']):
         vitorioso = 2
    elif all(numeros in escolhas_player1 for numeros in ['7', '8', '9']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['7', '8', '9']):
         vitorioso = 2
    elif all(numeros in escolhas_player1 for numeros in ['4', '5', '6']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['4', '5', '6']):
         vitorioso = 2
    elif all(numeros in escolhas_player1 for numeros in ['1', '2', '3']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['1', '2', '3']):
         vitorioso = 2
    elif all(numeros in escolhas_player1 for numeros in ['7', '4', '1']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['7', '4', '1']):
         vitorioso = 2
    elif all(numeros in escolhas_player1 for numeros in ['8', '5', '2']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['8', '5', '2']):
         vitorioso = 2
    elif all(numeros in escolhas_player1 for numeros in ['9', '6', '3']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['9', '6', '3']):
         vitorioso = 2
    elif all(numeros in escolhas_player1 for numeros in ['1', '5', '9']):
         vitorioso = 1
    elif all(numeros in escolhas_player2 for numeros in ['1', '5', '9']):
         vitorioso = 2   
