Total = 0
produtos = []
qtdes = []
preços = []
while True:
    produto = input('Produto: ')
    produtos.append(produto)
    qtde = int(input('quantidade: '))
    qtdes.append(qtde)
    preço = float(input('preço: '))
    preços.append(preço)
    Total = Total + qtde * preço

    s = input('Digite s para sair ou entrer para contiuar')
    if s.upper() == 'S':
       break
print('\n##########item da compra ##########')

for i in range(len(produtos)):
    print(f'intem {i+1}: {produtos[i]} - {qtdes[i]} * {preços[i]} = {qtdes[i]*preços[i]}')

print(f'total de compra: {Total}')

preço_etiqueta = float(input("Digite o preço de etiqueta:"))

codigo_pagamento = int(input("Digite o código de pagamento (1-4):"))

if codigo_pagamento == 1:
    valor_a_pagar = preço_etiqueta *0.9
elif codigo_pagamento == 2:
    valor_a_pagar = preço_etiqueta *0.85
elif codigo_pagamento == 3:
    total_a_pagar = round ( preço_etiqueta /2, 2)
    valor_a_pagar = preço_etiqueta
elif codigo_pagamento == 4:
    total_a_pagar = preço_etiqueta + 10/100 * preço_etiqueta
    total_a_pagar =  round (total_a_pagar / 3, 2)
    valor_a_pagar = preço_etiqueta*1.1
else:
    print("Código de pagamento inválido")

print("valor a ser: R$", valor_a_pagar)


