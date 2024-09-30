#Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
# Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

class Calculo:
    
    def soma (self,x,y):
        return x + y
    
    def subtracao (self,x,y):
        return x - y
x = 4
y = 5
Calculo = Calculo()
resultado_soma = Calculo.soma(x,y)
resultado_subtracao = Calculo.subtracao(x,y)   

print(f"Somando: {x}+{y} = {resultado_soma}")
print(f"Subtraindo: {x}-{y} = {resultado_subtracao}")