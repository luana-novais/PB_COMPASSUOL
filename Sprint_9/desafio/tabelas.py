import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as F
from pyspark.sql.functions import col, year, month, dayofmonth
from awsglue.job import Job


args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

parquet_path_1 = "s3://data-lake-luana-novais/Trusted/csv/2024/12/13/"
parquet_path_2 = "s3://data-lake-luana-novais/Trusted/json/"

parquet_data_1 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [parquet_path_1]}
)

parquet_data_2 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [parquet_path_2]}
)


parquet_df_1 = parquet_data_1.toDF()
parquet_df_2 = parquet_data_2.toDF()


df_result = parquet_df_1.join(parquet_df_2, parquet_df_1["id"] == parquet_df_2["imdb_id"], "inner").select(
    "imdb_id", "titulooriginal", "genero", "budget", "revenue", "notamedia", "numerovotos", 
    "release_date", "nomeartista", "personagem", "studio"
)


df_result = df_result.withColumn("revenue", col("revenue.int").cast("int"))
df_result = df_result.withColumn("numerovotos", col("numerovotos").cast("int"))


dim_genero = df_result.select("genero").distinct().withColumn("id_genero", F.monotonically_increasing_id())
dim_estudio = df_result.select("studio").distinct().withColumn("id_estudio", F.monotonically_increasing_id())
dim_personagem = df_result.select("personagem", "nomeartista").distinct().withColumn("id_personagem", F.monotonically_increasing_id())
dim_data = df_result \
    .select("release_date") \
    .distinct() \
    .withColumn("id_data", F.monotonically_increasing_id()) \
    .withColumn("ano", year(col("release_date"))) \
    .withColumn("mes", month(col("release_date"))) \
    .withColumn("dia", dayofmonth(col("release_date"))) \
    .withColumn("data", col("release_date").cast("string"))


fato_filmes = df_result \
    .join(dim_genero, "genero", "left") \
    .join(dim_estudio, "studio", "left") \
    .join(dim_personagem, "personagem", "left") \
    .join(dim_data, "release_date", "left") \
    .select(
        "imdb_id", "titulooriginal", "id_genero", "id_estudio", "id_personagem", 
        "id_data", "revenue", "notamedia", "numerovotos", "budget"
    )


dim_genero.write.mode("overwrite").parquet("s3://data-lake-luana-novais/Refined/dim_genero/")
dim_estudio.write.mode("overwrite").parquet("s3://data-lake-luana-novais/Refined/dim_estudio/")
dim_personagem.write.mode("overwrite").parquet("s3://data-lake-luana-novais/Refined/dim_personagem/")
dim_data.write.mode("overwrite").parquet("s3://data-lake-luana-novais/Refined/dim_data/")
fato_filmes.write.mode("overwrite").parquet("s3://data-lake-luana-novais/Refined/tabela_fato/")

job.commit()
