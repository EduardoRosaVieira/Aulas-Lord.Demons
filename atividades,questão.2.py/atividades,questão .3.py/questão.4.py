def calcular_idade(ano_corrente, ano_nascimento):
    idade = ano_corrente - ano_nascimento
    return idade
if __name__ == "__main__":
    ano_corrente = int(input("Digite o ano corrente: "))
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    
    idade = calcular_idade(ano_corrente, ano_nascimento)
    print(f"A idade da pessoa é: {idade} anos")