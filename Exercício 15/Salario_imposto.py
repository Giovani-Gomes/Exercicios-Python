Valor_hora = float(input("Informe quanto ganha por hora: "))
Horas_trabalhadas = int(input("Informe quantas horas você trabalhou: "))

Salario_Bruto= Horas_trabalhadas * Valor_hora
Valor_Imposto_Renda = (0.11 * Salario_Bruto)
Valor_INSS = (0.08 * Salario_Bruto)
Valor_Sindicato = (0.05 * Salario_Bruto)
Descontos = Valor_INSS + Valor_Imposto_Renda + Valor_Sindicato
Salario_liquido = Salario_Bruto - Descontos

print("*" * 30)
print("Salário Bruto :R${:.2f}".format(Salario_Bruto))
print("Imposto de Renda: R${:.2f}".format(Valor_Imposto_Renda))
print("INSS :R$ {:.2f}".format(Valor_INSS))
print("Sindicato :R${:.2f}".format(Valor_Sindicato))
print("Salário Liquido: R${:.2f}".format(Salario_liquido))
print("*" * 30)
