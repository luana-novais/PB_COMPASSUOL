# Função para ler o arquivo CSV 
def ler_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()  
    
    for i in range(1, len(linhas)):
        if "Robert Downey, Jr." in linhas[i]:
            linhas[i] = linhas[i].replace('"Robert Downey, Jr."', 'Robert Downey Jr')
    
    return [linha.strip().split(',') for linha in linhas]

# Escrever os arquivos
def escrever_em_arquivo(caminho, nome_arquivo, conteudo):
    caminho_completo = caminho + '/' + nome_arquivo
    with open(caminho_completo, 'w') as f:
        f.write(conteudo)

def etapa_1(dados, caminho):
    maior_filmes = 0
    ator_mais_filmes = ""
    
    for linha in dados[1:]:  # Ignorando o cabeçalho
        ator = linha[0]
        num_filmes = int(linha[2])  # Coluna "number of movies"
        if num_filmes > maior_filmes:
            maior_filmes = num_filmes
            ator_mais_filmes = ator
    
    resultado = f"O ator/atriz com mais filmes é {ator_mais_filmes} com {maior_filmes} filmes."
    escrever_em_arquivo(caminho, 'etapa-1.txt', resultado)

def etapa_2(dados, caminho):
    soma_gross = 0
    total_filmes = 0
    
    for linha in dados[1:]:  
        gross = float(linha[5])  # Coluna "gross"
        soma_gross += gross
        total_filmes += 1
    
    if total_filmes > 0:
        media_gross = soma_gross / total_filmes
        resultado = f"A média de receita bruta (gross) é: {media_gross:.2f}"
    else:
        resultado = "Não há filmes para calcular a média de receita bruta."
    
    escrever_em_arquivo(caminho, 'etapa-2.txt', resultado)

def etapa_3(dados, caminho):
    maior_media = 0
    ator_maior_media = ""
    
    for linha in dados[1:]:  
        ator = linha[0]
        media_por_filme = float(linha[3])  # Coluna "average per movie"
        if media_por_filme > maior_media:
            maior_media = media_por_filme
            ator_maior_media = ator
    
    resultado = f"O ator/atriz com a maior média de receita por filme é {ator_maior_media} com uma média de {maior_media:.2f}"
    escrever_em_arquivo(caminho, 'etapa-3.txt', resultado)

def etapa_4(dados, caminho):
    filmes = {}
    
    for linha in dados[1:]: 
        filme = linha[4]  # Coluna "movie"
        if filme in filmes:
            filmes[filme] += 1
        else:
            filmes[filme] = 1
    
    # Ordenar filmes por quantidade de aparições
    filmes_ordenados = sorted(filmes.items(), key=lambda x: x[1], reverse=True)
    
    resultado = ""
    for i, (filme, vezes) in enumerate(filmes_ordenados, 1):
        resultado += f"{i} - O filme '{filme}' aparece {vezes} vez(es) no dataset.\n"
    
    escrever_em_arquivo(caminho, 'etapa-4.txt', resultado)

def etapa_5(dados, caminho):
    receita_por_ator = {}
    
    for linha in dados[1:]:  
        ator = linha[0]
        receita = float(linha[1])  # Coluna "Total Gross"
        if ator in receita_por_ator:
            receita_por_ator[ator] += receita
        else:
            receita_por_ator[ator] = receita
    
    receita_ordenada = sorted(receita_por_ator.items(), key=lambda x: x[1], reverse=True)
    
    resultado = ""
    for ator, receita in receita_ordenada:
        resultado += f"{ator} - {receita:.2f}\n"
    
    escrever_em_arquivo(caminho, 'etapa-5.txt', resultado)

# Caminho onde os arquivos .txt serão salvos
caminho_para_salvar = '/home/luana/PB_LUANA_NOVAIS/Sprint_3/exercicios/seção-5/'  

# Carregar os dados do arquivo CSV
dados = ler_arquivo('/home/luana/PB_LUANA_NOVAIS/Sprint_3/exercicios/seção-5/actors.csv')  

# Executar as etapas
etapa_1(dados, caminho_para_salvar)
etapa_2(dados, caminho_para_salvar)
etapa_3(dados, caminho_para_salvar)
etapa_4(dados, caminho_para_salvar)
etapa_5(dados, caminho_para_salvar)
