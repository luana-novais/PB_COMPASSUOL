import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from datetime import datetime

bucket_name = 'data-lake-luana-novais'
movies_file = '/app/Sprint_6/desafio/movies.csv'
series_file = '/app/Sprint_6/desafio/series.csv'

session = boto3.Session(profile_name='779846783629_AdministratorAccess')

s3 = session.client('s3')

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

# Função para construir o caminho no S3 conforme o padrão exigido
def build_s3_path(data_origin, data_format, data_category, file_name):
    today = datetime.today()
    date_path = f"{today.year}/{today.month:02d}/{today.day:02d}"
    s3_path = f"Raw/{data_origin}/{data_format}/{data_category}/{date_path}/{file_name}"
    return s3_path

# Criar o bucket
create_bucket(bucket_name)

# Construir caminhos para cada arquivo e fazer o upload
movies_s3_path = build_s3_path("Local", "CSV", "Movies", "movies.csv")
series_s3_path = build_s3_path("Local", "CSV", "Series", "series.csv")

upload_s3(movies_file, bucket_name, movies_s3_path)
upload_s3(series_file, bucket_name, series_s3_path)
