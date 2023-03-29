class Pessoa:
    def __init__(self,nome,tel) -> None:
        self.nome = nome
        self.tel = tel

    def falar(self):
        print(f"{self.nome} Falou")

p1 = Pessoa("Alberto Roberto",99999999)
p1.falar() 

class Veterinario(Pessoa):
    pass

class Cliente(Pessoa):
    pass


v1 = Veterinario("Joao Silva", 88888888)
v1.falar()

cli = Cliente("Rodinei Souza", 77777777)
cli.falar()






































































































        




















