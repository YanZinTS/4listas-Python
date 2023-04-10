quantidade_cds = int(input("Quantos CDs você tem na sua coleção? "))
total_investido = 0

for i in range(1, quantidade_cds + 1):
    valor_cd = float(input("Digite o valor do CD {}: R$".format(i)))
    while valor_cd <= 0 or valor_cd > 1000:
        valor_cd = float(input("Digite um valor válido para o CD {}: R$".format(i)))
    total_investido += valor_cd

media_gasto = total_investido / quantidade_cds

print("O valor total investido em sua coleção de CDs é R${:.2f}.".format(total_investido))
print("O valor médio gasto em cada CD é R${:.2f}.".format(media_gasto))