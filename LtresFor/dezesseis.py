while True:
    n = int(input("Digite um número inteiro positivo e menor que 16 para calcular o fatorial: "))
    if n < 0 or n >= 16:
        print("Número inválido. Tente novamente.")
    else:
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i
        print(f"{n}! = {fatorial}")
        
    resposta = input("Deseja calcular outro fatorial? (S/N): ")
    if resposta.lower() == "n":
        break