class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3, taxa_chamada):
        self.matricula = matricula
        self.nome = nome
        self.notas = [nota1, nota2, nota3]
        self.taxa_chamada = taxa_chamada

    def __str__(self):
        return (f'Matrícula: {self.matricula}\n'
                f'Nome: {self.nome}\n'
                f'Notas: {self.notas}\n'
                f'Taxa de Chamada: {self.taxa_chamada}')

def main():
    alunos = []

    while True:
        matricula = input('Digite a matrícula do aluno: ')
        nome = input('Digite o nome do aluno: ')
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        taxa_chamada = float(input('Digite a taxa de chamada: '))

        aluno = Aluno(matricula, nome, nota1, nota2, nota3, taxa_chamada)
        alunos.append(aluno)

        continuar = input('Deseja adicionar outro aluno? (Digite "s" para sair ou qualquer tecla para continuar): ')
        if continuar.lower() == 's':
            break

    print('\nLista de Alunos:')
    for aluno in alunos:
        print('\n' + str(aluno))

if __name__ == "__main__":
    main()