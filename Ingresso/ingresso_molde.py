from class_ingresso import Ingresso

class Ingresso_opcao(Ingresso):
    def __init__(self, preco, setor,vip,normal) -> None:
        super().__init__(preco, setor)
        self.vip = vip
        self.normal = normal

    def v(self):
        print(f"Open Food: Incluso \nOpen Bar: Incluso \nEstacionamento: Incluso")

    def n(self):
        print(f"\nEstacionamento: Incluso")


 

i1 = input("Digite V para Ingresso vip ou N para ingresso normal: ") 
if i1 == "V":
    print(f"Ingresso vip")

ing = Ingresso_opcao(i1)


