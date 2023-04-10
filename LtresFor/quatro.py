while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("Nota inválida! Por favor, digite uma nota entre 0 e 10.")
    else:
        break
print("Nota válida: ", nota)