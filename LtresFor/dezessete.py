numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print("O número não é primo")
else:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print("O número é primo")
    else:
        print("O número não é primo")