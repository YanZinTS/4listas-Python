lados = int(input("Digite o número de lados: "))
medida = float(input("Digite a medida do lado: "))

if lados == 3:
    perimetro = medida * 3
    print("TRIÂNGULO, perímetro =", perimetro)
elif lados == 4:
    area = medida ** 2
    print("QUADRADO, área =", area)
elif lados == 5:
    print("PENTÁGONO")
elif lados < 3:
    print("Não é um polígono")
else:
    print("Polígono não foi encontardo")