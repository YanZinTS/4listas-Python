idaluno = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = float(input("Digite a média dos exercícios: "))

calc = (nota1 + nota2*2 + nota3*3 + media) / 7

if calc >= 9:
    conceito = "A"
    result = "APROVADO"
elif calc >= 7.5:
    conceito = "B"
    result = "APROVADO"
elif calc >= 6:
    conceito = "C"
    result = "APROVADO"
elif calc >= 4:
    conceito = "D"
    result = "REPROVADO"
else:
    conceito = "E"
    result = "REPROVADO"

print("Aluno:", idaluno)
print("Média de aproveitamento:", calc)
print("Conceito:", conceito)
print("Resultado:", result)