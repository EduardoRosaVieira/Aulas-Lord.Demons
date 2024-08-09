class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def desconto(self, percentual):
        """Aplica um desconto ao preço do produto e retorna o novo preço."""
        desconto = (percentual / 100) * self.preco
        preco_com_desconto = self.preco - desconto
        return preco_com_desconto

    def reajuste(self, percentual):
        """Aplica um reajuste ao preço do produto e retorna o novo preço."""
        reajuste = (percentual / 100) * self.preco
        preco_reajustado = self.preco + reajuste
        return preco_reajustado

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
            
            percentual_desconto = float(input('Digite o percentual de desconto: '))
            preco_com_desconto = produto.desconto(percentual_desconto)
            print(f'Preço com desconto: R${preco_com_desconto:.2f}')
            
            percentual_reajuste = float(input('Digite o percentual de reajuste: '))
            preco_reajustado = produto.reajuste(percentual_reajuste)
            print(f'Preço reajustado: R${preco_reajustado:.2f}')
            
        else:
            print('Produto não encontrado.')

def main():
    produtos = cadastrar_produtos()
    buscar_produto(produtos)

if __name__ == "__main__":
    main()