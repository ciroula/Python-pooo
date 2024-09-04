from abc import ABC, abstractmethod
import os 

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (
        f"\nLogradouro: {self.logradouro}"
        f"\nNumero: {self.numero}"
        f"\nCidade: {self.cidade}"
            )

class Funcionario(ABC):
    def __init__(self, nome: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.endereco = endereco
    
    @abstractmethod
    def salarioFinal(self) -> float: 
        pass

    def __str__(self)-> str:
        return (
            f"\nNome: {self.nome}"
            f"\nEmail: {self.email}"
            f"\nEndereco: {self.endereco}"
            f"\nSalario: {self.salarioFinal()}"
        )

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, email, endereco)

    def salarioFinal(self) -> float: 
        return 6000

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, email, endereco)
        self.cnh = cnh

    def salarioFinal(self) -> float: 
        return 6000

motoboy1 = Motoboy("jsdfsdjfijsd", "njfdsnfjdsnfm", "nfdsjnfjkdsn", 
                   Endereco("jdsnfndf", "fndjsfsknfm", "dksnfksdml"))

gerente1 = Gerente("dnsjkdfn", "jsdnfjsn", 
                   Endereco("njdsanjdnf", "jdsnjfnds", "njdksfdskf"))

print("=== Dados Motoboy ===")
print(f"Nome: {motoboy1.nome}")
print(f"email: {motoboy1.email}")
print(f"CNH: {motoboy1.cnh}")
print(f"Salario {motoboy1.salarioFinal()}")
print("\n")
print(f"Endereço: {motoboy1.endereco}")

print("\n")
print("=== Dados gerente ===")
print(f"Nome: {gerente1.nome}")
print(f"email: {gerente1.email}")
print(f"Salario {gerente1.salarioFinal()}")
print("\n")
print(f"Endereço: {gerente1.endereco}")