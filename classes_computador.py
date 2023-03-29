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
        self.valor = novo_preco


comp_modelo = Computador("Razer","Note2023","Core i5","12GB","250 GB SSD",3600,"3090 Super")
print("--Computador Modelo--")
comp_modelo.get_marca()
comp_modelo.get_ssd()
comp_modelo.get_placav()
comp_modelo.get_preco()

print("--Orçamento Do seu Computador--")
nom= input("Digite o a marca: ") 
ssd= input("Digite o SSD: ")    
comp1 = Computador(nom,"Note2023","Core i5","12GB",ssd,3600,"3090 Super")
#comp1.get_preco()

print("--Computador--")
comp1.set_preco(2900)
comp1.get_marca()
comp1.get_ssd()
comp1.get_placav()
comp1.get_preco()






