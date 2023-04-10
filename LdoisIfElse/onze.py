# Recebendo a data informada pelo usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Definindo uma variável booleana para armazenar se a data é válida ou não
data_valida = True

# Verificando se o mês está entre 1 e 12
if mes < 1 or mes > 12:
    data_valida = False
elif mes == 2:  # Caso o mês seja fevereiro
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):  # Verificando se o ano é bissexto
        if dia < 1 or dia > 29:
            data_valida = False
    else:  # Se não for bissexto
        if dia < 1 or dia > 28:
            data_valida = False
elif mes in (4, 6, 9, 11):  # Meses com 30 dias
    if dia < 1 or dia > 30:
        data_valida = False
else:  # Meses com 31 dias
    if dia < 1 or dia > 31:
        data_valida = False

# Imprimindo a mensagem correspondente
if data_valida:
    print("Data válida: {}/{}/{}".format(dia, mes, ano))
else:
    print("Data inválida!")