maior = float('-inf')
menor = float('inf')

while True:
    num = int(input("Digite um número inteiro (digite um número negativo para encerrar): "))
    if num < 0:
        break
    if num > maior:
        maior = num
    if num < menor:
        menor = num

if maior == float('-inf') or menor == float('inf'):
    print("Nenhum número válido foi digitado.")
else:
    print("O maior número digitado foi:", maior)
    print("O menor número digitado foi:", menor)