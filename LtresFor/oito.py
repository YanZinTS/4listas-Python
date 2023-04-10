capacidade_maxima = int(input("Digite a capacidade máxima do restaurante: "))
clientes_atual = 0

while clientes_atual < capacidade_maxima:
    clientes_chegaram = int(input("Digite a quantidade de clientes que chegaram: "))
    clientes_atual += clientes_chegaram
    if clientes_atual >= capacidade_maxima:
        print("Restaurante lotado, não há mais mesas disponíveis")