from pessoa_ex import Pessoa

class Professor(Pessoa):
    def __init__(self,matricula,nome, idade,formacao,disciplina,ch, sal) -> None:
        super().__init__(nome,matricula,idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.ch = ch
        self.sal = sal

    def get_f(self):
        print(f"Formação do professor: {self.formacao}")

    def get_d(self):
        print(f"Disciplina: {self.disciplina}")

    def get_c(self):
        print(f"Carga Horario do professor: {self.ch} minutos")

    def get_s(self):
        print(f"Salario: {self.sal} reais")

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade,estudar,*args) -> None:
        super().__init__(matricula, nome, idade)
        self.notas = args
        self.estudar = estudar
        self.media = 0


    def get_media(self):
        soma = sum(self.notas)
        self.media = soma/4
        print(f"Média: {self.media}")
        

    def get_e(self):
        print(f"{self.nome} ta estudando {self.estudar}")

print("-")
print("Aluno")
a1 = Aluno(16734,"Vinicius",17,"Matematica",7,9,8,8)
a1.get_m()
a1.get_n()
a1.get_i()
a1.get_e()
a1.get_media()

print("-")
print("Professor")
p1 = Professor("Chicão",0,40,"Havard","Física",200,20.000)
p1.get_n()
p1.get_i()
p1.get_f()
p1.get_d()
p1.get_c()
p1.get_s()    