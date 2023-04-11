salbruto = float(input("Informe o salário bruto: "))
proventos = float(input("Informe o valor dos proventos: "))

if salbruto <= 5000:
    desconto = salbruto * 0.05
else:
    desconto = salbruto * 0.1

salliquido = salbruto + proventos - desconto

print("O salário líquido é de: R$ {:.2f}".format(salliquido))