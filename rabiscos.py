nota1 = float(input("Digite a sua nota: "))
nota2 = float(input("Digite a sua nota: "))
nota3 = float(input("Digite a sua nota: "))
nota4 = float(input("Digite a sua nota: "))

calculo = nota1 + nota2 + nota3 + nota4
resultado = calculo / 4
media = (6.0)
if media >= 6.0:
    print(resultado, "Você está em recuperação!")
elif media <= 6.0:
    print(resultado, "Você está aprovado!")
else:
    print(resultado, "Você está reprovado!")