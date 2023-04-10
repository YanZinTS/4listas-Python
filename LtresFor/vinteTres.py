turmas = int(input("Quantidade de turmas: "))
total_alunos = 0

for i in range(1, turmas+1):
    while True:
        qtd_alunos = int(input(f"Quantidade de alunos na turma {i}: "))
        if qtd_alunos > 0 and qtd_alunos <= 40:
            total_alunos += qtd_alunos
            break
        else:
            print("Quantidade de alunos inválida. Digite um número entre 1 e 40.")

media = total_alunos / turmas
print(f"Média de alunos por turma: {media:.2f}")