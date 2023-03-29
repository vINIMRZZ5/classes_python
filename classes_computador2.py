class Computador:
    def __init__(self,marca,model,proc,ram,ssd,preco,placav) -> None:
        self.marca= marca
        self.model = model
        self.proc = proc
        self.ram = ram
        self.hd = ssd
        self.valor = preco
        self.placav = placav

    def get_marca(self):
        print(f"Marca: {self.marca}")
    
    def get_preco(self):
        print(f"Valor Atual: {self.valor}")
    
    def get_ssd(self):
        print(f"HD: {self.hd}")
    
    def get_placav(self):
        print(f"Placa de Video: {self.placav}")
    
    def set_preco(self,novo_preco):
        if novo_preco > 0:
            self.valor = novo_preco

    def set_marca(self,new):
        self.marca = new 



  
comp1 = Computador("Razer","Note2023","Core i5","12GB","250 SSD",3600,"3090 Super")
comp1.get_marca("Poitivo")
comp1.get_preco()

print("--Computador--")
comp1.set_preco(2900)
comp1.get_marca()
comp1.get_ssd()
comp1.get_placav()
comp1.get_preco()
