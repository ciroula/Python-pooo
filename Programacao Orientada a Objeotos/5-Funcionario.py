from abc import ABC, abstractmethod
import os 

os.system("cls || clear")

class Endereco(ABC) -> None:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str) -> None:
        self.nome = nome 
        self.telfone = telefone
        self.email = email
        self.endereco = Endereco

    @abstractmethod
    def salarioFinal(self) -> float:
        pass

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str) -> None:
        super().__init__(nome, telefone, email, endereco)

    def salarioFinal(self) -> float:
        

