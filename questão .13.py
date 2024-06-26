idade = int(input("digite sua idade:"))
if idade < 16:
    print(f'idade: {idade} - nao eleitor')
elif idade >= 18 and idade <= 65:
    print(f'idade: {idade} - eleitor obrigatorio')
else:
    print(f'idade: {idade} - eleitor facultativo')


