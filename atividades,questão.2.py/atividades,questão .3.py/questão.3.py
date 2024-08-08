def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
if __name__ == "__main__":
    num = int(input("Digite um número para mostrar a tabuada: "))
    tabuada(num)
    