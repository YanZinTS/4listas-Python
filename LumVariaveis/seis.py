salariom = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts gasta: "))

vquilowatt = salariom / 700
vpago = vquilowatt * quilowatts
vdesconto = vpago * 0.9

print(f"Valor em reais de cada quilowatt é de: R$ {vquilowatt:.2f}")
print(f"Valor a ser pago é: R$ {vpago:.2f}")
print(f"Valor com desconto de 10% é de: R$ {vdesconto:.2f}")
