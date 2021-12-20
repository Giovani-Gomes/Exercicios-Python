Peso_Peixes = float(input("Informe o Peso dos Peixes: "))
Excesso_Peixe = Peso_Peixes - 50

if Excesso_Peixe > 0:
    Multa =  int (Excesso_Peixe * 4)
    print("Você informou o Peso : {:.2f}Kg".format(Peso_Peixes))
    print("Excesso:  {:.2f} Kg".format(Excesso_Peixe))
    print("Valor da Multa :  R${:.2f}".format(Multa))
else:
    Multa = 0
    Excesso_Peixe = 0
    print("Você informou o Peso : {:.2f}Kg".format(Peso_Peixes))
    print("Excesso: {:.2f} Kg".format(Excesso_Peixe))
    print("Valor da Multa :  R${:.2f}".format(Multa))
