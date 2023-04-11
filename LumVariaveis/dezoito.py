qtd_fitas = int(input("Digite a quantidade de fitas: "))
valor_aluguel = float(input("Digite o valor do aluguel por fita: "))

faturamento_anual = (qtd_fitas / 3) * 12 * valor_aluguel
print("O faturamento anual da locadora é de R$", faturamento_anual)

multas_por_mes = (qtd_fitas / 30) * (valor_aluguel * 0.1)
print("O valor ganho com multas por mês é de R$", multas_por_mes)

fitas_estradas = qtd_fitas * 0.02
fitas_compradas = qtd_fitas * 0.1
qtd_fitas_final = qtd_fitas - fitas_estradas + fitas_compradas
print("A quantidade de fitas no final do ano será de", int(qtd_fitas_final), "fitas")