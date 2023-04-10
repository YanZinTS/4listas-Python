# Definindo a constante PI
PI = 3.1416

# Entrada do raio e altura da lata de óleo
raio = float(input("Digite o raio da lata de óleo: "))
altura = float(input("Digite a altura da lata de óleo: "))

# Cálculo do volume da lata de óleo
volume = PI * (raio ** 2) * altura

# Impressão do resultado
print(f"O volume da lata de óleo é: {volume:.2f}")