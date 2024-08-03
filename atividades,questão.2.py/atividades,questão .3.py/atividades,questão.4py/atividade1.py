def conceito(ma):
    if ma < 40:
        return 'E'
    elif ma < 60:
        return 'D'
    elif ma < 75:
        return 'C'
    elif ma < 90:
        return 'B'
    else:
        return 'A'
def resultado(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'APROVADO'
    else:
        return 'REPROVADO'
matricula = input('Digite a matricula:')
notal = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
ME = float(input('Digite a média de exercicios: '))
ma = (notal + nota2 * 2 + nota3 * 3 + ME) / 7
print('\n##############Resultados##############')
print(f'Matricula: (matricula)')
print(f'Nota 1: {notal} | nota 2: {nota2} | Nota 3: {nota3} | ME: {ME}')
print(f'Media de aproveitamento MA: {ma}')
print(f'conceito: {conceito(ma)}')
print(f'Resultado: {resultado(conceito(ma))}')


           

