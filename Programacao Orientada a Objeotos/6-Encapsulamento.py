import os 

os.system("cls || clear") #Limpar o terminal

#criando sua propia excecao.
class SaldoInsuficienteError(Exception):
    pass

#criando sua propia excecao.
class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numeroConta: int, agencia: int) -> None:
        self.numeroConta = numeroConta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido.

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        # try - except
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"

        self._saldo -= valor
        return self._saldo
    
    def __verificar_sacar(self, valor): #Metodo privado.
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")# Lancando um erro.
    
    def depositar(self, valor):
        try:
            self.__verificar_depositar(valor)
        except ValorNegativoError as error:
            return f"erro: `{error}"

        self._saldo += valor
        return self._saldo

    def __verificar_depositar(self, valor):
        if valor < 0:
            raise ValorNegativoError("Nao e possivel depositar valor negativo.")

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instaciar codigo
Conta_Corrente = ContaCorrente(222, 333)
Conta_Poupanca = ContaPoupanca(222, 333)

#print(Conta_Corrente._saldo) nao pode acontecer _saldo nao e permitido
print(Conta_Corrente.saldo)

print(Conta_Corrente.sacar(200))

print(Conta_Corrente.saldo) 

print(Conta_Corrente.depositar(-5))

print(Conta_Corrente.saldo)