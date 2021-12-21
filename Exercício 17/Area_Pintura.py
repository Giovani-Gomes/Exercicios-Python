Area_Quadrada=float(input("Informe em Metros Quadrados(m²) a Área que será pintada: "))
Consumo_Litros = Area_Quadrada / 6
print("*" * 50)
print("O consumo de tinta é {:.2f} litros".format(Consumo_Litros))
Quantidade_Latas_18 = Consumo_Litros / 18
Quantidade_Latas_36 = Consumo_Litros / 3.6
print("*" * 50)
print("a quantidade de Galôes de 18 LITROS a ser usado é: {:.2f}".format(Quantidade_Latas_18))
print("a quantidade de Galôes de 3,6 LITROS a ser usado é: {:.2f}".format(Quantidade_Latas_36))
valor_total_18 = Quantidade_Latas_18 * 80
valor_total_36 = Quantidade_Latas_36 * 25
print("*" * 50)
print("O valor total em GALOES de 18 LITROS é: R${:.2f}".format(valor_total_18))
print("O valor total em GALOES de 3,6 LITROS é:R${:.2f}".format(valor_total_36))
Quantidade_Latas_Mistas_18 =(((Consumo_Litros * 0.10) + Consumo_Litros) / 18)
Quantidade_Litros_18 = Quantidade_Latas_Mistas_18 * 18
Resto_18 =((Consumo_Litros * 0.10) + Consumo_Litros) - Quantidade_Litros_18
Quantidade_Latas_Mistas_36 =Resto_18 / 3.6
Quantidade_Latas_Mistas_Total = Quantidade_Latas_Mistas_18 + Quantidade_Latas_Mistas_36
Valor_misto_18 =Quantidade_Latas_Mistas_18 * 0.80
Valor_misto_36 = Quantidade_Latas_Mistas_36 * 25
Valor_misto_total = Valor_misto_18 + Valor_misto_36
print("*" * 50)
print("A quantidade de latas de 18 litros:{:.2f}".format(Quantidade_Latas_Mistas_18))
print("A quantidade de latas de 3,6 litros:{:.2f}".format(Quantidade_Latas_Mistas_36))
print("A quantidade de latas Mistas:{:.2f}".format(Quantidade_Latas_Mistas_Total))
print("A o valor total considerando GALOES e LATAS é (acresentando 10% de quebra): R${:.2f}".format(Valor_misto_total))
print("*" * 50)
