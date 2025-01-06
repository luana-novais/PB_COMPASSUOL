import json
import boto3
import requests

# Configurações da API
API_KEY = "1ef3edddb67953cd26eb8b04f19270ea"
BASE_URL_DISCOVER = "https://api.themoviedb.org/3/discover/movie"
BASE_URL_MOVIE = "https://api.themoviedb.org/3/movie"
GENRE_ID_SCI_FI = 878  # Gênero Science Fiction
S3_BUCKET_NAME = "data-lake-luana-novais"
S3_OUTPUT_KEY = "Raw/TMDB/JSON/2024/11/26/sci-fi-custos.json"

# Parâmetros para buscar filmes de sci-fi
discover_params = {
    "api_key": API_KEY,
    "language": "en-US",
    "with_genres": GENRE_ID_SCI_FI,
    "sort_by": "popularity.desc",
    "page": 1
}

# Função para buscar filmes de sci-fi
def fetch_sci_fi_movies():
    all_movies = []
    for page in range(1, 5):  
        discover_params["page"] = page
        try:
            response = requests.get(BASE_URL_DISCOVER, params=discover_params)
            response.raise_for_status()
            data = response.json()
            all_movies.extend(data.get("results", []))
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar filmes na página {page}: {e}")
            break
    return all_movies

# Função para buscar detalhes de um filme
def fetch_movie_details(movie_id):
    movie_details = {}
    try:
        response = requests.get(f"{BASE_URL_MOVIE}/{movie_id}", params={"api_key": API_KEY, "language": "en-US"})
        response.raise_for_status()
        movie_details = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes do filme ID {movie_id}: {e}")
    return movie_details

# Função para salvar os dados no S3
def save_to_s3(data):
    s3 = boto3.client('s3')
    try:
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=S3_OUTPUT_KEY,
            Body=json.dumps(data, ensure_ascii=False, indent=4),
            ContentType='application/json'
        )
        print(f"Dados salvos com sucesso em s3://{S3_BUCKET_NAME}/{S3_OUTPUT_KEY}")
    except Exception as e:
        print(f"Erro ao salvar os dados no S3: {e}")

# Função Lambda handler
def lambda_handler(event, context):
    sci_fi_movies = fetch_sci_fi_movies()
    detailed_movies = []

    for movie in sci_fi_movies:
        movie_id = movie.get("id")
        movie_details = fetch_movie_details(movie_id)
        if movie_details:
            detailed_movies.append({
                "id": movie_details.get("id"),
                "title": movie_details.get("title"),
                "budget": movie_details.get("budget"),  # Custo de produção
                "revenue": movie_details.get("revenue"),  # Receita
                "release_date": movie_details.get("release_date"),
                "genres": [genre["name"] for genre in movie_details.get("genres", [])],
            })

    # Salvar dados no S3
    save_to_s3(detailed_movies)

    return {
        'statusCode': 200,
        'body': json.dumps(f'{len(detailed_movies)} filmes salvos com sucesso.')
    }
