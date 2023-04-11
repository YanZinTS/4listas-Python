cod = int(input("Digite o código do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

maiornota = max(nota1, nota2, nota3)
media = (maiornota*4 + (nota1 + nota2 + nota3 - maiornota)*3)/10

print("O código do aluno é:", cod)
print("Notas:", nota1, nota2, nota3)
print("Média:", media)

if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")