# Projeto CountFinance - Sistema Financeiro

print()

print("Bem-Vindo(a) ao CountFinance!")

print("\n1-Cadastro\n2-Login\n3-Menu")

selecao = input("\nEscolha uma opção: ")

if selecao == "1":

    tipo_cadastro = input("Digite 'e' para email ou 'c' para CPF: ")

    if tipo_cadastro == "e":

        email = input("Digite seu email: ")
        email_confirmacao = input("Confirme seu email: ")

        if email == email_confirmacao:
            print("Email cadastrado com sucesso!")

    elif tipo_cadastro == "c":

        cpf = input("Digite seu CPF: ")
        cpf_confirmacao = input("Confirme seu CPF: ")

        if cpf == cpf_confirmacao:
            print("CPF cadastrado com sucesso!")

            senha = input("Crie uma senha: ")
        senha_confirmacao = input("Confirme sua senha: ")

        if senha == senha_confirmacao:
            print("CPF e senha cadastrados com sucesso!")
        else:
            print("As senhas não são iguais.")