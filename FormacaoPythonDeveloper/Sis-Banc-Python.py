menu = """
Qual operação você deseja realizar?
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower() 

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite_saque:
            print("Operação falhou! O valor do saque excede o limite diário.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Sessão encerrada.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
