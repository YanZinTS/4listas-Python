numero_conta = input("Digite o número da conta corrente de três dígitos: ")

# Inverte o número da conta
inverso = numero_conta[::-1]

# Soma o número da conta com o seu inverso
soma = int(numero_conta) + int(inverso)

# Calcula o dígito verificador
digito_verificador = sum(int(digito) * (i+1) for i, digito in enumerate(str(soma))) % 10

print("O dígito verificador da conta corrente é:", digito_verificador)