import math

PI = math.pi

raio = float(input("Digite o raio do círculo: "))

area = PI * raio**2

circunferencia = 2 * PI * raio

print(f"Área: {area:.2f}")
print(f"Circunferência: {circunferencia:.2f}")