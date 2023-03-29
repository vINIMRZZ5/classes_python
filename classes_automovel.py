class Automovel:
    def __init__(self,marca,nome,cor,envelopamento,motor,placa="HSB-9999") -> None:
        self.cor = cor
        self.placa = placa
        self.marca = marca
        self.nome = nome
        self.envelopamento = envelopamento
        self.motor = motor

    def dirigir(self,velocidade):
        print(f"Estou dirigindo a {velocidade} Km")

    def get_placa(self):
        print (self.placa)

    def get_cor(self):
        print(self.cor)
    
    def get_nome(self):
        print(self.nome)

    def get_marca(self):
        print(self.marca)

    def get_envelopamento(self):
        print(self.envelopamento)

    def get_motor(self):
        print(self.motor)

car1 = Automovel("Audi","A5","Preto","Carbono","2.0 - 4 Cilindros")
car1.get_placa()
car1.get_marca()
car1.get_nome()
car1.get_cor()
car1.get_envelopamento()
car1.get_motor()
car1.dirigir(250)


