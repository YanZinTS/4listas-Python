lados = int(input("Digite o número de lados do polígono: "))
medida = float(input("Digite a medida do lado do polígono: "))

if lados == 3:
    perimetro = medida * 3
    print("TRIANGULO, perímetro =", perimetro)
elif lados == 4:
    area = medida ** 2
    print("QUADRADO, área =", area)
elif lados == 5:
    print("PENTAGONO")
elif lados < 3:
    print("Não é polígono")
else:
    print("Polígono não identificado")