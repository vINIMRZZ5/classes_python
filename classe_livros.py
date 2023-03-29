class Livro:
    def __init__(self,nome,autor,editora,paginas) -> None:
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def get_nome(self):
        print(f"Nome: {self.nome}")

    def get_autor(self):
        print(f"autor: {self.autor}")
    
    def get_paginas(self):
        print(f"Páginas: {self.paginas}")

    def get_editora(self):
        print(f"Editora: {self.editora}")

    def set_editora(self,new):
        self.autor = new
    
livro1 = Livro("Por Lugares incriveis","Brett Haley","Suzy Elmiger",260)
livro1.get_nome()
livro1.get_autor()
livro1.get_editora()
livro1.get_paginas()
livro1.set_editora("Jennifer Niven")
print (f"Nova Editora: {livro1.autor}")