import boto3
from botocore.exceptions import NoCredentialsError, ClientError

bucket_name = 'ex-glue-ln'
file_name = '/home/luana/PB_LUANA_NOVAIS/Sprint_7/exercicios/LAB-Glue/nomes.csv'
s3_file_path = 'lab-glue/input/nomes.csv'

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

# Criar o bucket
create_bucket(bucket_name)

upload_s3(file_name, bucket_name, s3_file_path)
