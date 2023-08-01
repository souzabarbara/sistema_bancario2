class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    numero_conta = 0
    numero_agencia = "0001"

    def __init__(self, usuario):
        Conta.numero_conta += 1
        self.numero_conta = Conta.numero_conta
        self.numero_agencia = Conta.numero_agencia
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def deposito(self, valor):
        self.saldo += valor
        self.extrato += f"Depósito: R$ {valor:.2f}\n"

    def saque(self, *, valor):
        if self.numero_saques < self.LIMITE_SAQUES:
            if valor <= self.saldo and valor <= self.limite:
                self.saldo -= valor
                self.extrato += f"Saque: R$ {valor:.2f}\n"
                self.numero_saques += 1
            else:
                print("Operação falhou! Valor de saque inválido.")
        else:
            print("Operação falhou! Limite diário de saques atingido.")

    def extrato(self, *args, **kwargs):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


usuarios = []
contas = []


def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")
    cpf = input("Digite o CPF do usuário (apenas números): ")
    endereco = input(
        "Digite o endereço do usuário (logradouro, número - bairro - cidade/estado sigla): ")

    cpf_numeros = "".join(c for c in cpf if c.isdigit())

    for usuario in usuarios:
        if usuario.cpf == cpf_numeros:
            print("Já existe um usuário cadastrado com esse CPF.")
            return

    usuario = Usuario(nome, data_nascimento, cpf_numeros, endereco)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def cadastrar_conta():
    cpf = input(
        "Digite o CPF do usuário para vincular à conta (apenas números): ")
    cpf_numeros = "".join(c for c in cpf if c.isdigit())

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.cpf == cpf_numeros:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        conta = Conta(usuario_encontrado)
        contas.append(conta)
        print(
            f"Conta criada com sucesso! Agência: {conta.numero_agencia}, Conta: {conta.numero_conta}")
    else:
        print("Usuário não encontrado.")


def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            contas[0].deposito(valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            contas[0].saque(valor=valor)

        elif opcao == "e":
            contas[0].extrato()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    cadastrar_usuario()
    cadastrar_conta()
    main()
