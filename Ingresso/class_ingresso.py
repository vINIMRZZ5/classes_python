class Ingresso:
    def __init__(self,preco,setor) -> None:
     self.preco = preco
     self.setor = setor

    def get_preco(self):
       print(f"Preço do ingresso: {self.preco} reais")

    def set_preco(self):
       print(f"Novo preço do ingresso {self.preco} reais")

    def get_mostrar_setor(self):
       print(f"Setor: {self.setor}")