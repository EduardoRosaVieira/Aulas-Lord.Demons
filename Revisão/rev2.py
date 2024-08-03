preço_etiqueta = float(input("Digite o preço de etiqueta:"))

codigo_pagamento = int(input("Digite o código de pagamento (1-4):"))

if codigo_pagamento == 1:
    valor_a_pagar = preço_etiqueta *0.9
elif codigo_pagamento == 2:
    valor_a_pagar = preço_etiqueta *0.85
elif codigo_pagamento == 3:
    total = round ( preço_etiqueta /2, 2)
    valor_a_pagar = preço_etiqueta
elif codigo_pagamento == 4:
    total = preço_etiqueta + 10/100 * preço_etiqueta
    total =  round (total / 3, 2)
    valor_a_pagar = preço_etiqueta*1.1
else:
    print("Código de pagamento inválido")
print("valor a ser: R$", valor_a_pagar)








