while True:
    # Lê o nome de usuário e a senha
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Verifica se a senha é igual ao nome do usuário
    if senha == nome_usuario:
        print("A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Login realizado com sucesso!")
        break  # Sai do loop infinito