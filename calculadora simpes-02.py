# Calculadora simples em Python

def calculadora():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis: +  -  *  /")

    try:
        # Entrada dos números
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ").strip()
        num2 = float(input("Digite o segundo número: "))

        # Processamento
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                return
            resultado = num1 / num2
        else:
            print("Operador inválido.")
            return

        # Saída
        print(f"Resultado: {resultado}")

# Executa a calculadora
calculadora()