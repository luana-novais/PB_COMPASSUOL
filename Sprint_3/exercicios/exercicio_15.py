#Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
#liga(): muda o estado da lâmpada para ligada

#desliga(): muda o estado da lâmpada para desligada

#esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

#Para testar sua classe:
#Ligue a Lampada

#Imprima: A lâmpada está ligada? True

#Desligue a Lampada

#Imprima: A lâmpada ainda está ligada? False

class Lampada:

    def __init__(self, estado_inicial):
        self.ligada = estado_inicial
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada

lamp = Lampada(False)

lamp.liga()
print(f"A lâmpada está ligada? {lamp.esta_ligada()}")


lamp.desliga()
print(f"A lâmpada ainda está ligada? {lamp.esta_ligada()}")
