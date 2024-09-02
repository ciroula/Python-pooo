from abc import ABC, abstractmethod
import os 

os.system("cls || clear") #Limapar terminal.

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario 

    @abstractmethod
    def calcularSalario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcularSalario(self) -> float:
        BONIFICACAO = 1.2 #Equivale a 20%
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcularSalario(self) -> float:
        BONIFICACAO = 1.1 #Equivale a 20%
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal


#Instanciar classes

#Vai dar erro!!!
#funcionario1 = Funcionario("jose", 25, 50.0)
#print(f"Nome: {funcionario1.nome}")

gerente1 = Gerente("Marcia", 22, 2.500)
print(f"Nome: {gerente1.nome}")
print(f"Idade: {gerente1.idade}")
print(f"Gerente: {gerente1.calcularSalario()}")

motoboy1 = Motoboy("mai", 22, 2.500, "4586484654")
print("\n")
print(f"Nome: {motoboy1.nome}")
print(f"idade: {motoboy1.idade}")
print(f"Motoboy: {motoboy1.calcularSalario()}")
print(f"CNH: {motoboy1.cnh}")