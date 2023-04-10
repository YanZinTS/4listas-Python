candidatos = [0, 0, 0] # lista com o número de votos de cada candidato

n_eleitores = int(input("Digite o número total de eleitores: "))

for i in range(n_eleitores):
    voto = int(input(f"Eleitor {i+1}, vote em um candidato (1, 2 ou 3): "))
    candidatos[voto-1] += 1

print("Número de votos de cada candidato:")
print(f"Candidato 1: {candidatos[0]} votos")
print(f"Candidato 2: {candidatos[1]} votos")
print(f"Candidato 3: {candidatos[2]} votos")