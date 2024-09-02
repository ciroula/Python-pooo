import os
os.system("cls || clear") #Limpar o terminal

class Endereco:
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero
 
    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNumero: {self.numero}"
    #  def exibirEndereco (self) -> str:
    #     return f"\nLogradouro: {self.logradouro} \nNumero: {self.numero}"

    
class Aluno:
    #nome, idade
    #constructor

    def __init__(self, nome: str, idade: int, endereco: Endereco)-> None:
        #atribuidos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    #def exibir_dados(self) -> str:
    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}, \nEndereço: {self.endereco}"
    #    return f"Nome: {self.nome} \nIdade: {self.idade}, \nEndereço: {self.endereco.exibirEndereco()}"
    
# Instanciar classes
#endereco1 = Endereco("Tancredo", 4)
#aluno = Aluno("tancredo", 4, endereco1)

aluno1 = Aluno("Marta", 22, Endereco("Tancredo", 4))

#print(f"Nome: {aluno.nome}")
#print(f"Idade: {aluno.idade}")

print(aluno1)
#print(aluno1.exibir_dados())