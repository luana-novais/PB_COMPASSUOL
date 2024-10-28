import boto3
from botocore.exceptions import NoCredentialsError, ClientError

bucket_name = 'desafio-sprint5-luana-novais'
csv_file = 'Sprint_5/desafio/PALAS_OPERACOES_2022_06.csv'
s3_file_name = 'PALAS_OPERACOES_2022_06.csv'

# Criando o cliente do S3 
s3 = boto3.client('s3')

# Função para criar o bucket
def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)  
        print(f"Bucket '{bucket_name}' criado com sucesso.")
    except ClientError as e:
        print(f"Erro ao criar o bucket: {e}")

# Função para carregar o arquivo no bucket
def upload_s3(file_name, bucket, s3_file_name):
    try:
        s3.upload_file(file_name, bucket, s3_file_name)
        print(f"Arquivo '{file_name}' carregado com sucesso no bucket '{bucket}' como '{s3_file_name}'.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except NoCredentialsError:
        print("Credenciais não disponíveis.")
    except ClientError as e:
        print(f"Erro ao fazer o upload: {e}")

create_bucket(bucket_name)

upload_s3(csv_file, bucket_name, s3_file_name)
