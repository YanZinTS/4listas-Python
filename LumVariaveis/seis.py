salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts gasta pela residência: "))

valor_quilowatt = salario_minimo / 700
valor_pago = valor_quilowatt * quilowatts
valor_com_desconto = valor_pago * 0.9

print(f"Valor em reais de cada quilowatt: R$ {valor_quilowatt:.2f}")
print(f"Valor a ser pago: R$ {valor_pago:.2f}")
print(f"Valor com desconto de 10%: R$ {valor_com_desconto:.2f}")
