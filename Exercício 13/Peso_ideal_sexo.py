altura=float(input("Informe sua Altura: "))
sexo = str(input("Informe seu sexo: H - Homem || M - Mulher"))

if sexo == 'H' or sexo == 'h':
    Peso_ideal = (72.7*altura) -58
    print("Seu Peso ideal é {:.2f}".format(Peso_ideal))
elif sexo == 'M' or sexo == 'm':
    Peso_ideal = (62.1*altura) - 44.7
    print("Seu Peso ideal é {:.2f}".format(Peso_ideal))
else:
    print("Informe corretamente - H para HOMENS ou M para MULHERES")