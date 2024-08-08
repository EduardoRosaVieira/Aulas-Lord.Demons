lista_global = [1, 2, 3, 2, 4, 2, 5, 3, 6, 2]

def contar_ocorrencias(numero):
    quantidade = lista_global.count(numero)
    return quantidade
if __name__ == "__main__":
    num = int(input("Digite um número para contar suas ocorrências na lista: "))
    ocorrencias = contar_ocorrencias(num)
    print(f"O número {num} aparece {ocorrencias} vez(es) na lista global.")
    