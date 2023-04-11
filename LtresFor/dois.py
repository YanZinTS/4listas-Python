linhas = int(input("Digite o total de linhas da matriz: "))
colunas = int(input("Digite o total de colunas da matriz: "))

matriz = [[i+j for j in range(colunas)] for i in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        print("A{},{} = {}".format(i, j, matriz[i][j]), end="")
        if j == colunas-1:
            print("#")
        else:
            print(",", end=" ")
