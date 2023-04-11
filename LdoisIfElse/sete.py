sexo = input("Digite o sexo (m/f): ")
alt = float(input("Digite a altura em metros: "))

if sexo == 'm':
    peso_ideal = (72.7 * alt) - 58
    print("O peso ideal de um homem de altura {:.2f}m é de {:.2f}kg".format(alt, peso_ideal))
elif sexo == 'f':
    peso_ideal = (62.1 * alt) - 44.7
    print("O peso ideal de uma mulher de altura {:.2f}m é de {:.2f}kg".format(alt, peso_ideal))
else:
    print("esse sexo não existe")