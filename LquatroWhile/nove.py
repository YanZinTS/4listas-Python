candidatos = {
    1: "Branco",
    2: "Nulo",
    3: "Kiko",
    4: "Chaves",
    5: "Chiquinha"
}

votos = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

while True:
    voto = int(input("Digite o número do candidato (ou 666 para encerrar a votação): "))
    if voto == 666:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Candidato inválido.")

print("Resultado da votação:")
for candidato, votos_recebidos in votos.items():
    print(f"{candidatos[candidato]}: {votos_recebidos} votos")