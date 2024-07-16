def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

numero = int(input("Digite um número inteiro: "))
resultado = verificar_par_impar(numero)
print(resultado)