nconta = input("Digite o número de três dígitos: ")

inv = nconta[::-1]

soma = int(nconta) + int(inv)

verificador = sum(int(digito) * (i+1) for i, digito in enumerate(str(soma))) % 10

print("O dígito verificador da conta corrente é:", verificador)