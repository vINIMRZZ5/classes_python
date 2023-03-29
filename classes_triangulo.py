class Triangulo:
    def __init__(self,perimetro = None,) -> None:
        self.perimetro = perimetro
    def get_lados(self):
        return self.perimetro
    
info = Triangulo()
l1 = float(input("Digite o valor do 1° lado do triangulo: "))
l2 = float(input("Digite o valor do 2° lado do triangulo: "))
l3 = float(input("Digite o valor do 3° lado do triangulo: "))

if l1 > l2 or l1 > l3:
    print(f"Maior lado do triangulo: {l1}")
elif l2 > l1 or l2 > l3:
    print(f"Maior lado do triangulo: {l2}")
elif l3 > l1 or l3 > l2:
    print(f"Maior lado do triangulo: {l3}")


p = (l1+l2+l3)
print(f"Perimetro do triangulo: {p}")