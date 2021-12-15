import math
Num1 =int(input("Informe o Primeiro número Número Inteiro: "))
Num2 =int(input("Infome o Segundo Número Inteiro: "))
Num_real = float(input("Informe o Número Real: "))

Num1 = (Num1 * 2) + (Num2 / 2)
Num2 = (Num1 * 3 + Num_real)
Num_real = math.pow(Num_real,2)

print("O produto do dobro do primeiro com metade do segundo = {0}".format(Num1))
print("A soma do triplo do primeiro com o terceiro. = {0}".format(Num2))
print("O terceiro elevado ao cubo = {0} ".format(Num_real))
