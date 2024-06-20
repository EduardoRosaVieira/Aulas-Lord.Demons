sigla_estado = input("digite a sigla do estado do payton(ex: RJ, SP, MG):").upper()
if len(sigla_estado) != 2:
    print("sigla invalida. digite apenas duas leras.")
else:
    if sigla_estado == "RJ":
        print("O payton é carioca!")
    elif sigla_estado == "SP":
        print("O payton é paulista!")
    elif sigla_estado == "MG":
        print("O payton é mineiro!")
    else:
        print(f"O payton é de outro estado.")
        
              