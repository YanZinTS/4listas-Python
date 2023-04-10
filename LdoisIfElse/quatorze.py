# Ler os dados do aluno
id_aluno = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
me = float(input("Digite a média dos exercícios: "))

# Calcular a média de aproveitamento
ma = (nota1 + nota2*2 + nota3*3 + me) / 7

# Definir o conceito e resultado
if ma >= 9:
    conceito = "A"
    resultado = "APROVADO"
elif ma >= 7.5:
    conceito = "B"
    resultado = "APROVADO"
elif ma >= 6:
    conceito = "C"
    resultado = "APROVADO"
elif ma >= 4:
    conceito = "D"
    resultado = "REPROVADO"
else:
    conceito = "E"
    resultado = "REPROVADO"

# Imprimir os resultados
print("Aluno:", id_aluno)
print("Média de aproveitamento:", ma)
print("Conceito:", conceito)
print("Resultado:", resultado)