def calcular_valor_maximo(operadores,operandos) -> float:
    
    def aplicar_operacao(par_op_ope):
        operandos, operador = par_op_ope
        a, b = operandos
        
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            return a / b
        elif operador == '%':
            return a % b
        else:
            raise ValueError(f"Operador {operador} não suportado.")
    

    pares = zip(operandos, operadores)
    
    resultados = map(aplicar_operacao, pares)
    
    return max(resultados)

# Exemplo de uso:
operadores = ['+', '-', '*', '/', '+']
operandos  = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

maior_valor = calcular_valor_maximo(operadores, operandos)
print(maior_valor)  # Saída: 12
