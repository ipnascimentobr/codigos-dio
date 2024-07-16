# Solicitando os números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicitando a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realizando a operação matemática
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida.")
    exit()  # Encerra o programa se a operação for inválida

# Exibindo o resultado
print("O resultado da operação é:", resultado)
