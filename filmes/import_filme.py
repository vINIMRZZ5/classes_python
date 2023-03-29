class Filme:
    def __init__(self,nome,duracao) -> None:
        self.nome = nome
        self.duracao = duracao

    def iniciar(self):
        print(f"Foi iniciado o filme {self.nome}")

    def tempo(self):
        print(f"Duração: {self.duracao} Horas")
        
f1 = Filme("Harry Potter",2)
f1.iniciar()
