class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_realizados = 0  # contador para o número de saques realizados no dia

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_realizados < 3 and valor <= 500:
            if self.saldo >= valor:
                self.saldo -= valor
                self.extrato.append(f"Saque de R${valor:.2f}")
                self.saques_realizados += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite de saques diários atingido ou valor do saque excede R$ 500,00.")

    def ver_extrato(self):
        print("Extrato da conta:")
        
        if not self.extrato:
            print("Não foram realizadas movimentações.")
            print(f"Saldo atual: R${self.saldo:.2f}")
            return

        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}")


def main():
    conta = ContaBancaria()

    while True:
        print("\n1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor a ser depositado: R$"))
                conta.depositar(valor)
            except ValueError:
                print("Por favor, digite um valor válido.")
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor a ser sacado: R$"))
                conta.sacar(valor)
            except ValueError:
                print("Por favor, digite um valor válido.")
        elif opcao == '3':
            conta.ver_extrato()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
