import boto3
import pandas as pd
import numpy as np
from io import StringIO

# Função para ler arquivo do S3
def ler_csv_do_s3(bucket_name, s3_file_name):
    s3 = boto3.client('s3')
    csv_obj = s3.get_object(Bucket=bucket_name, Key=s3_file_name)
    conteudo_csv = csv_obj['Body'].read().decode('ISO-8859-1')  # Ajuste de encoding para ISO-8859-1
    return conteudo_csv

# Função para processar dados
def processar_dados(conteudo_csv):
    df = pd.read_csv(StringIO(conteudo_csv), sep=';', encoding='ISO-8859-1')

    # Filtrar dados usando dois operadores lógicos
    filtered_df = df[
        ((df['Qtd Prisao Preventiva'] > 0) | 
        (df['Qtd Mandado de Busca e Apreesao'] > 0)) & 
        (~df['Atuacao em Territorio Indigena'].str.contains('Sim'))
    ].copy()

    # Criar a coluna para verificar se há prisões em flagrante
    filtered_df['Ha_Prisao_Flagrante'] = np.where(filtered_df['Qtd Prisao em Flagrante'] > 0, 'Sim', 'Não')

    # Diferença de dias entre "Data do Início" e "Data da Deflagração"
    filtered_df['Data do Inicio'] = pd.to_datetime(filtered_df['Data do Inicio'], dayfirst=True)
    filtered_df['Data da Deflagracao'] = pd.to_datetime(filtered_df['Data da Deflagracao'], dayfirst=True)
    filtered_df['Diferenca_Dias'] = (filtered_df['Data da Deflagracao'] - filtered_df['Data do Inicio']).dt.days

    # Agrupar dados para calcular a quantidade de operações e o total de valores apreendidos
    grouped_df = filtered_df.groupby('Area').agg(

        Quantidade_de_Operacoes=('Area', 'size'),
        Total_Valores_Apreendidos=('Qtd Valores Apreendidos', lambda x: x.str.replace('R$', '', regex=False)
                                   .str.replace('.', '', regex=False)
                                   .str.replace(',', '.', regex=False)
                                   .astype(float).sum()),
        Ha_Prisao_Flagrante=('Ha_Prisao_Flagrante', lambda x: 'Sim' if 'Sim' in x.values else 'Não'),
        Media_Dias=('Diferenca_Dias', lambda x: int(x.mean())) 

    ).reset_index()

    # Criar o resultado final
    resultado_final = {
        "Quantidade de Operacoes por Area": grouped_df,
        "Quantidade Total de Dinheiro Apreendido": grouped_df['Total_Valores_Apreendidos'].sum(),
        "Houve prisão em Flagrante": filtered_df[['Area', 'Ha_Prisao_Flagrante']]
    }

    return resultado_final

# Função para salvar o resultado em um arquivo CSV
def salvar_resultado_csv(resultado, caminho_arquivo):
    df_final = resultado["Quantidade de Operacoes por Area"]
    
    df_final.to_csv(caminho_arquivo, index=False, sep=';', encoding='ISO-8859-1')
    print(f"Resultado salvo no arquivo {caminho_arquivo}")

# Função para fazer upload do arquivo CSV para o S3
def upload_csv_para_s3(bucket_name, caminho_arquivo, s3_file_name):
    s3 = boto3.client('s3')
    s3.upload_file(caminho_arquivo, bucket_name, s3_file_name)
    print(f"Arquivo {s3_file_name} enviado para o bucket {bucket_name}.")

bucket_name = 'desafio-sprint5-luana-novais'
s3_file_name = 'PALAS_OPERACOES_2022_06.csv'
conteudo_csv = ler_csv_do_s3(bucket_name, s3_file_name)

# Processa os dados
resultado = processar_dados(conteudo_csv)

# Salva o resultado em um arquivo CSV local
caminho_arquivo_local = 'Sprint_5/desafio/desafioresultado_final.csv'
salvar_resultado_csv(resultado, caminho_arquivo_local)

# Faz o upload do arquivo para o S3
upload_csv_para_s3(bucket_name, caminho_arquivo_local, 'resultado_final.csv')