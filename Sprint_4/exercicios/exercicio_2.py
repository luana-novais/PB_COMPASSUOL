def conta_vogais(texto: str) -> int:
    vogais = 'aeiou' 
    qtd_vogais = filter(lambda c: c.lower() in vogais, texto)
  
    return len(list(qtd_vogais))

texto = "Ola mundo, este e um importante teste"
print(conta_vogais(texto))