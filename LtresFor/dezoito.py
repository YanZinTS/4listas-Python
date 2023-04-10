num = int(input("Digite um número inteiro: "))

divisores = []

for i in range(2, num):
    if num % i == 0:
        divisores.append(i)

if len(divisores) == 0:
    print(num, "é um número primo")
else:
    print(num, "não é um número primo")
    print("Divisores:", divisores)