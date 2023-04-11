vlr = float(input("Digite o valor da prestação em atraso: "))
tx = float(input("Digite a taxa de juros ao mês: "))
tempo = int(input("Digite o tempo de atraso em meses: "))

prestacao = vlr + (vlr * (tx/100) * tempo)

print(f"O valor total da prestação em atraso é de: R${prestacao:.2f}")