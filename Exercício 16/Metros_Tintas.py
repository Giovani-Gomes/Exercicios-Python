
Area_Quadrada =float(input("Informe a Área Quadrada em que pretende Pintar: "))
Litros = Area_Quadrada / 3

Latas = (Litros / 18)
Total = (Latas * 80.00)

print("Você usará {:.2f} de Tintas.".format(Latas))
print("O preço total é R${:.2f}".format(Total))
