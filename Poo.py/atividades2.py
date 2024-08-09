class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return (f'Código: {self.codigo}\n'
                f'Nome: {self.nome}\n'
                f'Preço: R${self.preco:.2f}\n'
                f'Quantidade: {self.quantidade}')

def cadastrar_produtos():
    produtos = {}

    while True:
        codigo = input('Digite o código do produto: ')
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input('Digite a quantidade do produto: '))

        produto = Produto(codigo, nome, preco, quantidade)
        produtos[codigo] = produto

        continuar = input('Deseja cadastrar outro produto? (Digite "s" para sair ou qualquer tecla para continuar): ')
        if continuar.lower() == 's':
            break

    return produtos

def buscar_produto(produtos):
    while True:
        codigo_busca = input('Digite o código do produto para buscar ou "s" para sair: ')
        if codigo_busca.lower() == 's':
            break

        produto = produtos.get(codigo_busca)
        if produto:
            print('\nProduto Encontrado:')
            print(produto)
        else:
            print('Produto não encontrado.')

def main():
    produtos = cadastrar_produtos()
    buscar_produto(produtos)

if __name__ == "__main__":
    main()