# leitura dos valores de A e B
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# verificação se A é divisível por B
if a % b == 0:
    print(a, "é divisível por", b)
else:
    print(a, "não é divisível por", b)