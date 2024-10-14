import csv

def calcular_media(notas):
    return round(sum(notas) / len(notas), 2)

def formatar_nota(media):
   
    if media.is_integer():
        return f"{media:.1f}"  
    else:
        return f"{media:.2f}"

def processar_notas(arquivo):
    dados = []

    with open(arquivo, mode='r', encoding='utf-8') as file:
        estudantes = csv.reader(file)

        for linha in estudantes:
            nome = linha[0]
            notas = list(map(int, linha[1:]))

            notas_maiores = sorted(notas, reverse=True)[:3]
            media = calcular_media(notas_maiores)

            dados.append((nome, notas_maiores, media))

    dados.sort(key=lambda x: x[0])

    for nome, notas_maiores, media in dados:
        notas_formatadas = ', '.join(map(str, notas_maiores))
        media_formatada = formatar_nota(media)
        print(f"Nome: {nome} Notas: [{notas_formatadas}] Média: {media_formatada}")

processar_notas("estudantes.csv")