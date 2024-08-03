numeros = []
indice = 0
numero = int(input('digite um número: '))
numeros.append(numero)
maior = numero
for n in range(1,10):
    numero = int(input('digite um numero: '))
    numeros.append(numero)
    if maior < numero:
        meior = numero
        indice = n
        print(f'lista dos numeros: {numeros}')
        print(f'maior numero: {maior} - seu indice é: {indice}')
