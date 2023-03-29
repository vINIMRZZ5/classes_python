class Pessoa:
    def __init__(self,matricula,nome,idade) -> None:
        self.matricula = matricula
        self.nome = nome
        self.idade = idade 

    def get_m(self):
        print(f"Matricula: {self.matricula}")

    def get_n(self):
        print(f"Nome: {self.nome}")

    def get_i(self):
        print(f"Idade: {self.idade}")