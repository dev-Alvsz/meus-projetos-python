# Porta abre e fecha c/ senha

porta_aberta = True
if porta_aberta:
    print("A porta está aberta")
    senha = input("Digite a senha para abrir a porta: ")
    if senha == "1234":
        print("Acesso liberado")
    else:
        if senha != "1234":
            print("Acesso negado, tente novamente!")