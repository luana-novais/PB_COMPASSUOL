animais = [ "Cachorro", "Gato", "Leão", "Tigre", "Elefante", "Girafa", "Urso", 
    "Lobo", "Raposa", "Coelho", "Panda", "Zebra", "Canguru", "Golfinho", 
    "Baleia", "Tubarão", "Papagaio", "Aguia", "Coruja", "Cavalo"
]

[print(animal) for animal in sorted(animais)]

with open("/home/luana/PB_LUANA_NOVAIS/Sprint_8/exercicios/geração-massa-dados/animals.csv", "w") as file:
    for animal in sorted(animais):
        file.write(f"{animal}\n")

print("\nOs nomes dos animais foram salvos no arquivo 'animals.csv'.")