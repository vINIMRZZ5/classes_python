from animal import Animal

class Peixe(Animal):
    def __init__(self, name, color,peso) -> None:
        super().__init__(name, color)
        self.peso = peso

    def mover(self):
        print(f"{self.name} Nadou")

    def nadar(self):
        print("Squashhsh")

if __name__ == "__main__":
    print("-")
    a1 = Animal("Humble","Cinza")
    a1.mover()

    print("-")
    p1 = Peixe("Nemo","Vermelho Listrado",5)
    p1.mover()
    p1.nadar()