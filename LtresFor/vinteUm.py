n = int(input("Digite o número de pessoas na turma: "))
idades = []

for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

media = sum(idades) / n

if media >= 0 and media <= 25:
    print("A turma é jovem")
elif media >= 26 and media <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")