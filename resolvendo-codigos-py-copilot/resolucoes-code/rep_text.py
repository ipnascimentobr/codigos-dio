def repetir_string():
    # Solicita a string e o número inteiro como entrada
    string = input("Digite uma string: ")
    numero = int(input("Digite um número inteiro: "))
    
    # Retorna a string repetida o número de vezes informado
    resultado = string * numero
    return resultado

# Exemplo de uso
resultado = repetir_string()
print(resultado)
