linhas = int(input("Digite o total de linhas da matriz: "))
colunas = int(input("Digite o total de colunas da matriz: "))

# Preenchendo a matriz com valores aleatórios apenas para exemplificar a impressão
matriz = [[i+j for j in range(colunas)] for i in range(linhas)]

# Imprimindo a matriz com o padrão especificado
for i in range(linhas):
    for j in range(colunas):
        print("A{},{} = {}".format(i, j, matriz[i][j]), end="")
        if j == colunas-1:
            print("#")
        else:
            print(",", end=" ")
