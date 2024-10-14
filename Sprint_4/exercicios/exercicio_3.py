from functools import reduce

def calcula_saldo(lancamentos) -> float:
    
    soma = list(map(lambda x: x[0] if x[1] == "C" else -x[0], lancamentos))
    saldo_final = reduce(lambda x, y: x + y, soma)
    return saldo_final
    
    
    
lancamentos = [(200,'D'),(300,'C'),(100,'C')]
saldo = calcula_saldo(lancamentos)
print(saldo)