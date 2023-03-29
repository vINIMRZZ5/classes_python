class Calculadora:
    pass
    def calcular(self,opcao,num1,num2):
        if opcao == "+":
            return self.__adicionar(num1,num2)
        elif opcao == "-":
            return self.__subtrair(num1,num2)
        else:
            print("Opção invalida!")

    def __adicionar(self,n1,n2):
            return n1+n2
        
    def __subtrair(self,n1,n2):
            return n1,n2


a = float(input("Digite seu numero: "))
a1 = float(input("Digite seu outro numero: "))
calc = Calculadora()
result = calc.calcular("+",a,a1)
print(result)



































