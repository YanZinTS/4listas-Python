import math

# Entrada dos catetos do triângulo retângulo
cateto1 = float(input("Digite a medida do primeiro cateto: "))
cateto2 = float(input("Digite a medida do segundo cateto: "))

# Cálculo da hipotenusa
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

# Impressão do resultado
print(f"Hipotenusa: {hipotenusa}")