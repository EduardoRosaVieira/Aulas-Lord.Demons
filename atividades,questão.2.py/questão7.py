menor_altura = float('inf')
maior_altura = float('-inf')
for i in range(15):
    altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))
    if altura<menor_altura:
        menor_altura = altura
        if altura>maior_altura:
            maior_altura = altura
            print("A menor altura é:", menor_altura)
            print("A maior altura é:",maior_altura)
