import math

cateto1 = float(input("Digite a medida do primeiro cateto: "))
cateto2 = float(input("Digite a medida do segundo cateto: "))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print(f"Hipotenusa: {hipotenusa}")