import json
import boto3
import requests
from datetime import datetime

# Configurações da API
API_KEY = "1ef3edddb67953cd26eb8b04f19270ea"
BASE_URL_DISCOVER = "https://api.themoviedb.org/3/discover/movie"
BASE_URL_MOVIE = "https://api.themoviedb.org/3/movie"
GENRE_ID_SCI_FI = 878
MARVEL_STUDIO_ID = 420
S3_BUCKET_NAME = "data-lake-luana-novais"

# Função para gerar chave de saída no S3
def generate_s3_output_key():
    today = datetime.today()
    date_str = today.strftime('%Y/%m/%d')
    return f"Raw/TMDB/JSON/{date_str}/marvel-sci-fi-movies.json"

def fetch_marvel_sci_fi_movies():
    all_movies = []
    page = 1 
    while True:
        discover_params = {
            "api_key": API_KEY,
            "language": "en-US",
            "with_genres": GENRE_ID_SCI_FI,
            "with_companies": MARVEL_STUDIO_ID,  
            "sort_by": "popularity.desc",
            "page": page,
        }

        try:
            response = requests.get(BASE_URL_DISCOVER, params=discover_params)
            response.raise_for_status()
            data = response.json()
            movies = data.get("results", [])
            all_movies.extend(movies)

            if data.get("page") < data.get("total_pages"):
                page += 1  
            else:
                break  

        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar filmes: {e}")
            break

    return all_movies

# Função para buscar detalhes de um filme
def fetch_movie_details(movie_id):
    try:
        response = requests.get(f"{BASE_URL_MOVIE}/{movie_id}", params={"api_key": API_KEY, "language": "en-US"})
        response.raise_for_status()
        movie_details = response.json()

        studio_name = None
        for company in movie_details.get("production_companies", []):
            if company.get("id") == MARVEL_STUDIO_ID: 
                studio_name = company.get("name", "Desconhecido") 
                break

        return {
            "id": movie_details.get("id"),
            "title": movie_details.get("title"),
            "imdb_id": movie_details.get("imdb_id"),
            "budget": movie_details.get("budget"),
            "revenue": movie_details.get("revenue"),
            "release_date": movie_details.get("release_date"),
            "studio": studio_name,  
            "genres": [genre["name"] for genre in movie_details.get("genres", [])]
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes do filme ID {movie_id}: {e}")
        return None

# Função para salvar os dados no S3
def save_to_s3(data, key):
    s3 = boto3.client('s3')
    try:
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=key,
            Body=json.dumps(data, ensure_ascii=False, indent=4),
            ContentType='application/json'
        )
        print(f"Dados salvos com sucesso em s3://{S3_BUCKET_NAME}/{key}")
    except Exception as e:
        print(f"Erro ao salvar os dados no S3: {e}")

# Função Lambda handler
def lambda_handler(event, context):

    marvel_sci_fi_movies = fetch_marvel_sci_fi_movies()
    detailed_movies = []

    for movie in marvel_sci_fi_movies:
        movie_id = movie.get("id")
        movie_details = fetch_movie_details(movie_id)
        if movie_details:
            detailed_movies.append(movie_details)

    if not detailed_movies:
        return {
            'statusCode': 400,
            'body': json.dumps("Nenhum filme da Marvel de sci-fi foi encontrado ou processado.")
        }


    s3_key = generate_s3_output_key()
    save_to_s3(detailed_movies, s3_key)

    return {
        'statusCode': 200,
        'body': json.dumps(f'{len(detailed_movies)} filmes da Marvel de Sci-Fi salvos com sucesso.')
    }
