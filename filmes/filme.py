from import_filme import Filme
class Acao(Filme):
    pass
    def acao(self):
        print("Gênero: Ação")

class Drama(Filme):
    pass
    def d(self):
        print("Gênero: Drama")

class Suspense(Filme):
    pass
    def s(self):    
        print(f"Gênero: Suspense")

class Terror(Filme):
    pass
    def t(self):    
        print("Gênero: Terror")

print("-")
f2 = Acao("Spider Man No way Home",3)
f2.iniciar()
f2.acao()


print("-")
f3 = Drama("As vantagens de ser invisivel",2)
f3.iniciar()
f3.d()


print("-")
f4 = Suspense("Stranger Things",20)
f4.iniciar()
f4.s()


print("-")
f5 = Terror("Scream 6",2)
f5.iniciar()
f5.t()
