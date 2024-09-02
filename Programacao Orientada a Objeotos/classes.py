import os
os.system("cls || clear") #Limpar o terminal

class Aluno:
    #nome, idade
    #constructor

    def __init__(self, nome, idade)-> None:
        #atribuidos
        self.nome = nome
        self.idade = idade

   def exibir_dados(self)
        return f"Nome: {self.nome} \nIdade: {self.idade}"
    
# Instanciar classes
#print(f"Nome: {aluno.nome}")
#print(f"Idade: {aluno.idade}")
aluno = Aluno("Marta", 22)

print(aluno.exibir_dados())