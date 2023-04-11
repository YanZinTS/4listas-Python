while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha == nome_usuario:
        print("A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Login realizado com sucesso!")
        break 