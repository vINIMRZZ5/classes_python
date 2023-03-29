class Animal:
    def __init__(self,name,color) -> None:
        self.name = name
        self.color = color

    def mover(self):
        print(f"{self.name} Andou")

a1 = Animal("Estrela","Blonde")
a1.mover()

class Cachorro(Animal):
    pass
    def latir(self):
        print("AuAU")

class Gato(Animal):
    pass
    def mia(self):
        print("Miau Miau")

class Coelho(Animal):
    pass
    def pular(self):
        print("Puf Puf")

class Peixe(Animal):
    def __init__(self, name, color,peso) -> None:
        super().__init__(name, color)
        self.peso = peso

    def mover(self):
        print(f" {self.__name} Nadou...")
        
print("-")
c1 = Cachorro("Irelia","Golden")
c1.mover()
c1.latir()

print("-")
cat1 = Gato("Lily","preto")
cat1.mover()
cat1.mia()

print("-")
c2 = Coelho("Yasuo", "Cinza")
c2.mover()
c2.pular()