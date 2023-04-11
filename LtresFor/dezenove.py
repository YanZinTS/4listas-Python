n = int(input("Digite um número inteiro N: "))

numeros = list(range(2, n+1))

num_divisoes = 0

for i in range(2, int(n**0.5)+1):
    if i in numeros:
        for j in range(i*i, n+1, i):
            num_divisoes += 1
            if j in numeros:
                numeros.remove(j)

print("Números primos encontrados:", numeros)
print("Número de divisões realizadas:", num_divisoes)