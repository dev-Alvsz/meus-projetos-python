print()

print("Bem-Vindo(a) ao CountFinance!")

cpf = ""
senha = ""

# ======================= MENU =========================
while True:

    print("\n===== COUNTFINANCE =====")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")

    selecao = input("\nEscolha uma opção: ")

    if selecao == "1":

        tipo_cadastro = input("Digite 'e' para email ou 'c' para CPF: ")

        if tipo_cadastro == "e":

            email = input("Digite seu email: ")
            email_confirmacao = input("Confirme seu email: ")

            if email == email_confirmacao:

                senha = input("Digite sua senha: ")
                senha_confirmacao = input("Confirme sua senha: ")

                if senha == senha_confirmacao:
                    print("\nEmail e senha cadastradas com sucesso!")

                else:
                    print("\nAs senhas não são iguais.")

            else:
                print("\nOs emails não são iguais.")

        elif tipo_cadastro == "c":

            cpf = input("Digite seu CPF: ")
            cpf_confirmacao = input("Confirme seu CPF: ")

            if cpf == cpf_confirmacao:

                senha = input("Crie uma senha: ")
                senha_confirmacao = input("Confirme sua senha: ")

                if senha == senha_confirmacao:
                    print("\nCPF e senha cadastradas com sucesso!")

                else:
                    print("\nAs senhas não são iguais!")

            else:
                print("\nOs CPFs não são iguais!")

# ============================ login =====================================

    elif selecao == "2":

     print("\n===== LOGIN =====")
     print("1 - Entrar com CPF")
     print("2 - Entrar com Email")

    tipo_login = input("\nEscolha uma opção: ")

    if tipo_login == "1":

        cpf_login = input("Digite seu CPF: ")
        senha_login = input("Digite sua senha: ")

        if cpf_login == cpf and senha_login == senha:
            print("\nLogin realizado com sucesso!")
            print("Bem-vindo ao CountFinance!")
        else:
            print("\nCPF ou senha incorretos.")

    elif tipo_login == "2":

        email_login = input("Digite seu email: ")
        senha_login = input("Digite sua senha: ")

        if email_login == email and senha_login == senha:
            print("\nLogin realizado com sucesso!")

        else:
            print("\nEmail ou senha incorretos.")

    else:

        print("\nAceso Negado!")

# ================== Sair ===================================


while selecao == "3":

    print("\nSaindo do CountFinance...")
    break

# ===================== TELA DE INICIO ============================

print("")