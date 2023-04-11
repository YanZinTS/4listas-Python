a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if b == 0:
    print("Não dividi", a, "por zero")
else:
    if a % b == 0:
        print(a, "é divisível por", b)
    else:
        print(a, "não é divisível por", b)