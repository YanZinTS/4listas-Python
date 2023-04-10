salario_bruto = float(input("Informe o salário bruto: "))
proventos = float(input("Informe o valor dos proventos: "))

if salario_bruto <= 5000:
    desconto = salario_bruto * 0.05
else:
    desconto = salario_bruto * 0.1

salario_liquido = salario_bruto + proventos - desconto

print("Salário líquido: R$ {:.2f}".format(salario_liquido))