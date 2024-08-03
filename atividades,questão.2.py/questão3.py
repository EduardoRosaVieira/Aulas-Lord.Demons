contador = 0
while True:
    numero = int(input("Digite um numero positivo ou negativo para parar): "))
    if numero <= 0:
        break
    contador += 1
    print("Voc~e digitou", contador, "numero positivos.")