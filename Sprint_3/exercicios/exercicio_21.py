#Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.

#Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.

#Imprima no console exatamente assim:
#Pato
#Voando...
#Pato emitindo som...
#Quack Quack
#Pardal
#Voando...
#Pardal emitindo som...
#Piu Piu

class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass
    def voar(self):
        pass

class Pato(Passaro):
    def emitir_som(self):
        print('Quack Quack')

class Pardal(Passaro):
    def emitir_som(self):
        print('Piu Piu')

        
pato = Pato(nome='Pato')
pardal = Pardal(nome='Pardal')


print(pato.nome)
pato.voar()
print(f'{pato.nome} emitindo som...')
pato.emitir_som()


print(pardal.nome)
pardal.voar()
print(f'{pardal.nome} emitindo som...')
pardal.emitir_som()
