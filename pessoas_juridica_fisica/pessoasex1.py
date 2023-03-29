from pessoaex import Pessoa

class Juridico(Pessoa):
    def __init__(self, nome, telefone, email, endereco,cnpj,compra) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.compra = compra

    def get_cnpj(self):
        print(f"CNPJ: {self.cnpj}")

    def get_desconto(compra):
        print("Desconto de 25%")

class Fisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco,cpf,compra) -> None:
        super().__init__(nome, telefone, email, endereco)

        self.cpf = cpf
        self.compra = compra


    def get_cpf(self):
        print(f"CPF: {self.cpf}")
        

    def get_desconto(compra):
        print("Desconto de 15%")

print("Cadastros da Fornecedora")
print("Pessoa Juridica")
pessoa1 = Juridico("Luciano",67995648586,"lucian.opgg@gmai.com","R.noxus","897.848.8784/0001-47","Peças")
pessoa1.get_nome()
pessoa1.get_telefone()
pessoa1.get_email()
pessoa1.get_cnpj()
pessoa1.get_desconto()

print("-")
print("Pessoa Fisica")
pessoa2 = Fisica("Senna",67995847956,"senna.opgg@gmai.com","R.noxus","639.000.677.84","Peças")
pessoa2.get_nome()
pessoa2.get_telefone()
pessoa2.get_email()
pessoa2.get_cpf()
pessoa2.get_desconto()

print("-")
opcao = int(input("Digite 1 para negociar ou 0 para sair: "))
if opcao == 1:
    peça = input("Digite a peça que deseja comprar: ")
    carro = input("Qual o modelo do carro: ")
    j_n = input("Digite J/N para Juridica ou Fisica: ").upper()
    if j_n == "J" or "j":
        print("Negociação em analise com 25% de desconto")
    else:
        print("Negociação com 15% de desconto")
else:
    print("Negociação encerrada")







