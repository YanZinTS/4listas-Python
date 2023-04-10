limite_inferior = float(input("Digite o limite inferior em Celsius: "))
limite_superior = float(input("Digite o limite superior em Celsius: "))
decremento = float(input("Digite o decremento em Celsius: "))

print("Celsius\tFahrenheit")
celsius = limite_inferior
while celsius <= limite_superior:
    fahrenheit = (celsius * 9/5) + 32
    print("{:.1f}\t{:.1f}".format(celsius, fahrenheit))
    celsius += decremento