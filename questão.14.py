a =int(input("informe o valor de a: "))
b =int(input("informe o valor de b: "))
c =int(input("informe o valor de c: "))
delta = a*b - 4*a*c # b**2
if delta < 0:
    print(f'delta: {delta} - nao ha raizes')
    if delta == 0:
        print(f'delta: {delta} - nao e equaçao do segundo grau')
    else:
        raiz1 = (-b + (delta**0.5)) / 2*a
        raiz2 = (-b + (delta**0.5)) / 2*a
        print(f'delta: {delta} - raiz 1: {raiz1}, raiz 2: {raiz2}')

