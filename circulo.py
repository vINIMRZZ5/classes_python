class Circulo:
    def _init_(self, raio= None, area= None) -> None:
        self.raio = raio
        self.area = area 

    def raio(self, circunferencia):
        return circunferencia

    def area(self, area):
        return area
        
info = Circulo()
raio = float(input("Digite o valor do raio, para obter a circuferência e a área do círculo: "))


circunferencia = 2 * 3.14 * raio
area = 3.14 * (raio * raio)
print(f"Raio: {raio}")
print("A circuferência do círculo: {:.2f}".format(circunferencia))
print("A área do círculo: {:.2f}".format(area))