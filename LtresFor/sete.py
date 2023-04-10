# inicializa as variáveis para os dois primeiros termos da série
a = 0
b = 1

# imprime o primeiro termo
print(a)

# imprime o segundo termo
print(b)

# enquanto o último termo da série for menor ou igual a 500
while b <= 500:
    # calcula o próximo termo da série
    c = a + b
    
    # imprime o próximo termo da série
    print(c)
    
    # atualiza as variáveis para os próximos cálculos
    a = b
    b = c