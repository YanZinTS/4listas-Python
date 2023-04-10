sexo = input("Digite o sexo (M/F): ")
altura = float(input("Digite a altura em metros: "))

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem de altura {:.2f}m é {:.2f}kg".format(altura, peso_ideal))
elif sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher de altura {:.2f}m é {:.2f}kg".format(altura, peso_ideal))
else:
    print("Sexo inválido.")