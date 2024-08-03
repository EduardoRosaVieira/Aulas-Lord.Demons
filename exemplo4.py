altura = float(input('digite a altura: '))
sexo = input('digite o sexo: ')
if (sexo.upper() == 'M'): # lower
    pesoideal = (72.7*altura)-58
else:
    pesoideal = (62.1*altura)-44.7
print('O sexo informado foi: ', sexo.upper())
print('Seu peso ideal é: ', pesoideal)



