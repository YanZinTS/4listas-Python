n = int(input("Digite um número inteiro N: "))

# Criando uma lista de números de 1 a N
numeros = list(range(2, n+1))

# Inicializando o número de divisões com 0
num_divisoes = 0

# Percorrendo todos os números de 2 a raiz de N
for i in range(2, int(n**0.5)+1):
    # Se o número atual está na lista de números, elimina seus múltiplos
    if i in numeros:
        for j in range(i*i, n+1, i):
            num_divisoes += 1
            if j in numeros:
                numeros.remove(j)

# Imprimindo os números primos encontrados e o número de divisões realizadas
print("Números primos encontrados:", numeros)
print("Número de divisões realizadas:", num_divisoes)