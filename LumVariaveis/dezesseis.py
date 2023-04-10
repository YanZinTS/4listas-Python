# Entrada dos valores da prestação em atraso
valor = float(input("Digite o valor da prestação em atraso: "))
taxa = float(input("Digite a taxa de juros ao mês (%): "))
tempo = int(input("Digite o tempo de atraso em meses: "))

# Cálculo do valor total da prestação
prestacao = valor + (valor * (taxa/100) * tempo)

# Impressão do resultado
print(f"O valor total da prestação em atraso é: R${prestacao:.2f}")