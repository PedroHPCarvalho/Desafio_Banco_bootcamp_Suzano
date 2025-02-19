from abc import ABC, abstractmethod
from datetime import date


class Conta():
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico):
        self.__saldo: float = saldo
        self.__numero: int = numero
        self.__agencia: str = agencia
        self.__cliente: Cliente = cliente
        self.__historico: Historico = historico

    def saldo(self):
        pass
  
    def sacar(self, valor: float):
        pass

    def depositar(self, valor: float):
        pass


class ContaCorrente(Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico, limite: float, limite_saques: int):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.__limite: float = limite
        self.__limite_saques: int = limite_saques


class Cliente():
    def __init__(self, endereco: str, contas: list):
        self.__endereco: str = endereco
        self.__contas: list = contas

    def realizar_transacao(conta: Conta, transacao: Transacao):
        pass
    

    def adicionar_contas(conta: Conta):
        pass


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, contas: list, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco, contas)
        self.__cpf: str = cpf
        self.__nome: str = nome
        self.__data_nascimento: date = data_nascimento
 

class Historico():
    def __init__(self):
        pass
    
    def adicionar_transacao(transacao: Transacao):
        

class Transacao(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass
    

class Saque(Transacao):
    def __init__(self, valor: float):
        self.__valor: float = valor
    

    def registrar(self, conta: Conta):
        pass
    

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.__valor: float = valor
    

    def registrar(self, conta: Conta):
        pass