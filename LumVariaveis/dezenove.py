numero_conta = input("Digite o número da conta corrente de três dígitos: ")

inverso = numero_conta[::-1]

soma = int(numero_conta) + int(inverso)

digito_verificador = sum(int(digito) * (i+1) for i, digito in enumerate(str(soma))) % 10

print("O dígito verificador da conta corrente é:", digito_verificador)