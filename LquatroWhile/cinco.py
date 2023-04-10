limite_inferior = int(input("Digite o limite inferior do intervalo: "))
limite_superior = int(input("Digite o limite superior do intervalo: "))
incremento = int(input("Digite o incremento: "))

# Verifica se o incremento é positivo
if incremento <= 0:
    print("O incremento deve ser um número positivo!")
else:
    # Imprime os números inteiros do intervalo de acordo com o incremento
    i = limite_inferior
    while i <= limite_superior:
        print(i)
        i += incremento