#  04 - Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Verifica até a raiz quadrada de n
        if n % i == 0:
            return False
    return True

for num in range(1,101):
    if primo(num):
        print(num)    
    