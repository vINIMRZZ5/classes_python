class Pessoa:
    def __init__(self,nome,telefone,email,endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
       

    def get_nome(self):
        print(f"Nome: {self.nome}")

    def get_telefone(self):
        print(f"Telefone: {self.telefone}")

    def get_email(self):
        print(f"E-mail: {self.email}")

    def get_endereco(self):
        print(f"Endereço: {self.endereco}")

    def get_obter_desconto(self):
        print(f"Solicitou um desconto")





    