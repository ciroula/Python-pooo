import os 

os.system("cls || clear") # Limpar o terminal 

class Livro:
    #Titulo, Autor, Numero de Paginas e o Preço
    #Constructor

    def __init__(self, titulo, autor, numeroDePaginas, preco) -> None:
        #Atribuidos
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.preco = preco

    def exibirDados(self):
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nNumer de paginas {self.numeroDePaginas} \nPreço: {self.preco}"

#Instanciar classes
livro1 = Livro("Maravilha", "Mic", 22, 5.20)
livro2 = Livro("Qualquer um", "Mic", 26, 6.60)

#print(f"Autor: {Livro.titulo}")
#print(f"Titulo: {Livro.autor}")
#print(f"_____: {Livro.____}")
#print(f"_____: {Livro.____}")
print(livro1.exibirDados())
print(livro2.exibirDados())