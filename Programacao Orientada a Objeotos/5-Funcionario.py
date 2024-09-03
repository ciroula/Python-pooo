from abc import ABC, abstractmethod
import os 

os.system("cls || clear")

class Endereco(ABC):
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nlogradouro: {self.logradouro}"
            f"\nnumero: {self.numero}"
            f"\ncomplemento: {self.complemento}"
            f"\ncep: {self.cep}"
            f"\ncidade: {self.cidade}"
        )

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome 
        self.telfone = telefone
        self.email = email
        self.endereco = endereco

    @classmethod
    def salarioFinal(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\ntelefone: {self.telefone}"
            f"\nemail: {self.email}"
            f"\nendereco: {self.endereco}"
            f"\salario: {self.salarioFinal()}"
        )

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salarioFinal(self) -> float:
        return 5.000
    
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
    
    def salarioFinal(self) -> float:
        return 5.000
    
engenheiro1 = Engenheiro("sjdfnsdnmf", "busdhfsd", "bsdjhfgjsdn", "bdbfjsd",
                         Endereco("jsadnfjsdn", "jdnsfjnds", "jnsafjsdnf", "bjhesadfjsn", "nfjsdnfds"))
print("===Dados do Engenheiro===")
print(f"Nome: {engenheiro1.nome}") 
print(f"Telefone: {engenheiro1.telfone}")
print(f"Email: {engenheiro1.email}")
print(f"CREA: {engenheiro1.crea}")
print("\n")
print("===Dados do Usuario===")
print(f"Endereco: {engenheiro1.endereco}")
print(f"salario: {engenheiro1.salarioFinal()}")

medico1 = Medico("sjdfnsdnmf", "busdhfsd", "bsdjhfgjsdn", "bdbfjsd",
                         Endereco("jsadnfjsdn", "jdnsfjnds", "jnsafjsdnf", "bjhesadfjsn", "nfjsdnfds"))
print("\n")
print("===Dados do Medico===")
print(f"Nome: {medico1.nome}") 
print(f"Telefone: {medico1.telfone}")
print(f"Email: {medico1.email}")
print(f"CREA: {medico1.crm}")
print("\n")
print("===Dados do Usuario===")
print(f"Endereco: {medico1.endereco}")
print(f"salario: {medico1.salarioFinal()}")
        

