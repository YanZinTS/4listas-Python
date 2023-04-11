n = int(input("Quantidade de números: "))

menor = 10**9
maior = -10**9
soma = 0

for i in range(n):
    num = int(input("Digite um número: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma += num

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)