import math

# Declaração da constante PI
PI = math.pi

# Entrada do raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Cálculo da área do círculo
area = PI * raio**2

# Cálculo do comprimento da circunferência
circunferencia = 2 * PI * raio

# Impressão dos resultados
print(f"Área: {area:.2f}")
print(f"Circunferência: {circunferencia:.2f}")