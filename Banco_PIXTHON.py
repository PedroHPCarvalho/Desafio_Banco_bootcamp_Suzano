Conta = "P-1234"
saldo_atual = 0.0
Qtd_Saque = 0
Historico_Operações = list()
Lista_Usuarios = list()
Contas_Correntes = list()


def criar_usuario(nome, nro_conta):
    global Lista_Usuarios
    Lista_Usuarios.append(dict([('nome', nome), ('nro_conta', nro_conta)]))
    print("Usuario Criado")


def criar_conta_corrente(Lista_Usuarios, nro_conta):
    conta_corrente = {
        "nome": Lista_Usuarios["nome"],
        "nro_conta": nro_conta,
        "saldo"
    }
    


def depositar(saldo_dep):
    global saldo_atual
    global Historico_Operações
    saldo_atual = saldo_atual + saldo_dep
    Historico_Operações.append(dict({('Operação', 'deposito'), ('Valor da Operação', saldo_dep), ('Saldo Atual', saldo_atual)}))
    return None


def saque(valor_saque):
    global saldo_atual
    global Qtd_Saque
    global Historico_Operações

    if Qtd_Saque == 3:
        print("Seu limite de 3 saques diarios foi atingido")
    else:
        if valor_saque > 500:
            print("Limite de saque é de 500")
        else:
            if valor_saque > saldo_atual:
                print("Sem Saldo")
            else:
                saldo_atual = saldo_atual - valor_saque
                Qtd_Saque += 1
                print("Saque feito com Sucesso")
                Historico_Operações.append(dict({('Operação', 'saque'), ('Valor da Operação', valor_saque), ('Saldo Atual', saldo_atual)}))


def extrato():
    global Historico_Operações
    for i in enumerate(Historico_Operações):
        print([i])


criar_usuario("Pedro", "0-001")
print(Lista_Usuarios)
criar_conta_corrente("0-001")