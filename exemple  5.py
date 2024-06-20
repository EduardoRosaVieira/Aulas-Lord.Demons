contador = 0
contF = 0
contM = 0
mediaF = 0
mediaM = 0.0
maior = 0
menor = 99
qtde = int(input('Digite = quantidade de alunos: '))

while contador <= 5:
    sexo = input('digite o sexo: ')
    altura = float('digite a altura: ')
    if sexo.upper() == 'F' :
        contF = contF + 1
        mediaF = mediaF +altura
    elif sexo.upper() == 'M':
        contM = contM + 1
        mediaM = mediaM + altura
    else:
        print('Sexo informado é invalido.')
        continue
contador = contador + 1
print('A quantidade de alunos do sexo feminino é: ', contF)
print('A quantidade de alunos do sexo masculino é: ', contM)
if contM > 0:
    mediaM = mediaM / contM

    print('A média de alturas do sexo feminino é: ', mediaF)
    print('A média de altura do sexo masculino é: ', mediaM)
    
    print('A maior altura é: ', maior)
    print('A menor altura é: ', menor)




