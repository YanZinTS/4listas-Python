idade = int(input("Digite a idade do trabalhador: "))
tempservico = int(input("Digite o tempo de serviço em anos: "))

if idade >= 65 or tempservico >= 30 or (idade >= 60 and tempservico >= 25):
    print("O trabalhador pode se aposentar")
else:
    print("O trabalhador não pode se aposentar")