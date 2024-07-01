import textwrap
import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente, numero_conta):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        transacao = Deposito(valor)
        transacao.efetuar(self)
        self.extrato.append(transacao)

    def sacar(self, valor, limite=500, limite_saques=3):
        transacao = Saque(valor)
        transacao.efetuar(self, limite, limite_saques)
        self.extrato.append(transacao)

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não há movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


class ContaCorrente(Conta):
    def __init__(self, cliente, numero_conta):
        super().__init__(cliente, numero_conta)
        self.limite = 500

class Transacao:
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.datetime.now()

class Deposito(Transacao):
    def efetuar(self, conta):
        conta.saldo += self.valor

    def __str__(self):
        return f"{self.data} - Depósito: R$ {self.valor:.2f}"

class Saque(Transacao):
    def efetuar(self, conta, limite, limite_saques):
        if self.valor > conta.saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        elif self.valor > limite:
            print("\n@@@ Operação falhou! Valor de saque excede o limite permitido. @@@")
        elif conta.numero_saques >= limite_saques:
            print("\n@@@ Operação falhou! Limite máximo de saques diários atingido. @@@")
        else:
            conta.saldo -= self.valor
            conta.numero_saques += 1

    def __str__(self):
        return f"{self.data} - Saque: R$ {self.valor:.2f}"

class MenuBanco:
    def __init__(self):
        self.opcoes = {
            'd': "Depositar",
            's': "Sacar",
            'e': "Extrato",
            'nc': "Nova conta",
            'lc': "Listar contas",
            'nu': "Novo usuário",
            'q': "Sair"
        }
        self.contas = []
        self.usuarios = []
        self.proxima_conta = 1

    def exibir_menu(self):
        menu_text = """
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu_text)).strip().lower()

    def depositar(self, conta):
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("\n@@@ Valor inválido! Por favor, insira um número válido. @@@")
            return
        
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return
        
        conta.depositar(valor)
        print("\n=== Depósito realizado com sucesso! ===")

    def sacar(self, conta):
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("\n@@@ Valor inválido! Por favor, insira um número válido. @@@")
            return
        
        conta.sacar(valor)
        print("\n=== Saque realizado com sucesso! ===")

    def exibir_extrato(self, conta):
        conta.exibir_extrato()

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if not cpf.isdigit() or len(cpf) != 11:
            print("\n@@@ CPF inválido! Informe um CPF válido com 11 dígitos numéricos. @@@")
            return
        
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("\n@@@ Já existe usuário com esse CPF! @@@")
                return
        
        nome = input("Informe o nome completo: ")
        cliente = Cliente(nome, cpf)
        self.usuarios.append(cliente)
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário para associar à conta: ")
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)
        
        if not usuario:
            print("\n@@@ Usuário não encontrado! Cadastre o usuário antes de criar a conta. @@@")
            return
        
        conta = ContaCorrente(usuario, self.proxima_conta)
        self.contas.append(conta)
        self.proxima_conta += 1
        print("\n=== Conta criada com sucesso! ===")

    def listar_contas(self):
        if not self.contas:
            print("\n=== Não há contas cadastradas no sistema. ===")
            return
        
        print("\n================ LISTA DE CONTAS ================")
        for conta in self.contas:
            print(f"""
                Agência: {AGENCIA}
                C/C: {conta.numero_conta}
                Titular: {conta.cliente.nome}
                Saldo: R$ {conta.saldo:.2f}
                Número de Saques: {conta.numero_saques}
            """)
        print("==================================================")


    def main(self):
        while True:
            opcao = self.exibir_menu()

            if opcao == "d":
                self.depositar()
            elif opcao == "s":
                self.sacar()
            elif opcao == "e":
                self.exibir_extrato()
            elif opcao == "nu":
                self.criar_usuario()
            elif opcao == "nc":
                self.criar_conta()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "q":
                print("\n=== Encerrando o programa... ===")
                break
            else:
                print("\n@@@ Operação inválida! Selecione uma opção válida do menu. @@@")
                continue

if __name__ == "__main__":
    menu_banco = MenuBanco()
    menu_banco.main()
