cont1 = 0
cont2 = 0
cont3 = 0
cont0 = 0
cont4 = 0
while True:
    volto = int(input('digite o seu volto (1, 2, 3 . para canditados, 0 para branco e 4 para nulo): ' ))
    if volto == 1:
        cont1 += 1 # cont1 = cont1 + 1
    elif volto == 2:
        cont2 += 1
    elif volto == 3:
        cont3 += 1
    elif volto == 4:
        cont4 += 1
    elif volto == 0:
        cont0 += 1
    elif volto == -1:
        break
    else:
        print('informe um codigo valido.')

if cont1 > cont2 and cont2 > cont3:
    print(f'o canditado 1 é vencedor com {cont1} volto.')
elif cont2 > cont1 and cont1 > cont3:
    print(f'o canditado 2 é o vencedor com {cont2} voltos.')
else:
    print(f'O canditado 3 é o vencedor com {cont3} voltos.')
    
    print(f'O número de voltos nulos: {cont4}')

    print(f'O número de eleitores que compareceram ás urnas: {cont0 + cont1 + cont2 + cont3 + cont4}')

