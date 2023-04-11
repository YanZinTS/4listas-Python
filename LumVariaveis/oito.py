import math

PI = math.pi

raio = float(input("Digite o raio do círculo: "))

area = PI * raio**2

circunferencia = 2 * PI * raio

print(f"A área é: {area:.2f}")
print(f"A circunferência é: {circunferencia:.2f}")