ano_nascimento =int(input("digite o ano de nascimento do payton: "))
ano_atual =int(input("digite o ano atual:"))
if ano_nascimento < 0 or ano_nascimento > ano_atual:
    print("ano de nascimento invalido.")
else:
    idade = ano_atual - ano_nascimento
    print(f"O payton tem {idade} anos de idade.")
    
