# Recebendo a data informada pelo usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Definindo uma variável booleana para armazenar se a data é válida ou não
data_valida = True

if mes < 1 or mes > 12:
    datvalida = False
elif mes == 2:  
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0): #verifica se o ano é bissexto
        if dia < 1 or dia > 29:
            datvalida = False
    else:  #se caso não for bissexto
        if dia < 1 or dia > 28:
            datvalida = False
elif mes in (4, 6, 9, 11):  #os meses com 30 dias
    if dia < 1 or dia > 30:
        datvalida = False
else:  #os meses com 31 dias
    if dia < 1 or dia > 31:
        datvalida = False

if datvalida:
    print("Data válida: {}/{}/{}".format(dia, mes, ano))
else:
    print("Data inválida!")