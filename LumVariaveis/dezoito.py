qtdfitas = int(input("Digite a quantidade de fitas: "))
valuguel = float(input("Digite o valor do aluguel por fita: "))

faturamentoa = (qtdfitas / 3) * 12 * valuguel
print("O faturamento anual da locadora é de R$", faturamentoa)

multames = (qtdfitas / 30) * (valuguel * 0.1)
print("O valor ganho com multas por mês é de R$", multames)

festradas = qtdfitas * 0.02
fcompradas = qtdfitas * 0.1
qtdfitastotal = qtdfitas - festradas + fcompradas
print("A quantidade de fitas no final do ano será de", int(qtdfitastotal), "fitas")