limite_superior = float(input("Digite o limite superior do intervalo: "))
incremento = float(input("Digite o incremento: "))

print("Fahrenheit\tCelsius")

for f in range(10, int(limite_superior) + 1, int(incremento)):
    c = (f - 32) * 5/9
    print(f"{f}\t\t{c:.2f}")