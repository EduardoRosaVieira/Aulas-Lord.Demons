contador_maiores = 0
for i in range(10):
    idade = int(input("Digite a idade da pessoa {}:".format(i+1)))
    if idade >= 18:
        contador_maiores += 1
        print("A quantidade de pessoas maiores de idade é:",contador_maiores)
        