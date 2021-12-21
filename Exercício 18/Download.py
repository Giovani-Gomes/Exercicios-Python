Tamanho_arquivo = float(input("Informe do tamanho do arquivo em MegaByte: "))
Velocidade_link = float(input("Informe a velocidade do link em Mbps: "))
Tempo_Aproximado = ((Tamanho_arquivo * 8) / Velocidade_link) / 60

if Tempo_Aproximado < 1.00:
    print("O tempo aproximado de download é de {:.2f} segundos".format(Tempo_Aproximado))
elif Tempo_Aproximado > 1.00:
    print("O tempo aproximado de download é de {:.2f} minutos".format(Tempo_Aproximado))
else:
    print('Impossível calcular o tempo')