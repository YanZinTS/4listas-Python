# Inicializando as variáveis
qtd_alunos_terceira = 0
maior_qtd_livros_quarta = 0
qtd_nao_gosta_redacao_terceira = 0
qtd_alunos = 0

# Loop para leitura dos dados
while True:
    serie = int(input("Digite a série do aluno (1 a 4, digite 0 para encerrar): "))
    if serie == 0:
        break
    qtd_livros = int(input("Digite a quantidade de livros que o aluno lê por mês: "))
    gostar_redacao = int(input("O aluno gosta de fazer redação? (1 - sim, 0 - não): "))
    
    # Incrementando a quantidade de alunos na terceira série
    if serie == 3:
        qtd_alunos_terceira += 1
    
    # Verificando a maior quantidade de livros lidos por um aluno da quarta série
    if serie == 4 and qtd_livros > maior_qtd_livros_quarta:
        maior_qtd_livros_quarta = qtd_livros
    
    # Verificando se o aluno não gosta de fazer redação e está na terceira série
    if serie == 3 and gostar_redacao == 0:
        qtd_nao_gosta_redacao_terceira += 1
    
    # Incrementando a quantidade total de alunos
    qtd_alunos += 1

# Calculando a porcentagem de alunos que não gostam de redação e estão na terceira série
if qtd_alunos_terceira > 0:
    porcentagem_nao_gosta_redacao_terceira = (qtd_nao_gosta_redacao_terceira / qtd_alunos_terceira) * 100
else:
    porcentagem_nao_gosta_redacao_terceira = 0

# Imprimindo os resultados
print("Quantidade de alunos na terceira série:", qtd_alunos_terceira)
print("Maior quantidade de livros lidos por um aluno da quarta série:", maior_qtd_livros_quarta)
print("Porcentagem de alunos que não gostam de fazer redação e que estão na terceira série:", porcentagem_nao_gosta_redacao_terceira, "%")