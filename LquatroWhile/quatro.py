n = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range(1, n+1):
    soma += 2*i
print("A soma dos", n, "primeiros números pares é:", soma)