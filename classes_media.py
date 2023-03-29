class Alunos:
    def __init__(self,nome,ra,total) -> None:
        self.nome = nome
        self.ra = ra
        self.total = total
       

    def get_nome(self):
        print(f"Nome: {self.nome}")

    def get_ra(self):
        print(f"RA: {self.ra}")

    def get_total(self):
        print(f"Nota final: {self.total}")

n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))
n4 = int(input("Digite a nota 4: "))
total = (n1+n2+n3+n4)/4

aluno1 = Alunos("Vinicius","19734",total)
aluno1.get_nome()
aluno1.get_ra()  
aluno1.get_total()     

if total >= 7:
    print("Resultado: Aprovado")

elif total >= 5 or total <= 6.9:
    print("Resultado: Exame Final")

elif total < 5:
    print("Resultado: Reprovado")
