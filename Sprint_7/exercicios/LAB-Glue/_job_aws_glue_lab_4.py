import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.functions import upper, count, desc, col, when
from pyspark.sql.types import IntegerType

# Parâmetros do Job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de origem e destino
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Ler o arquivo CSV
df = spark.read.option("header", "true").option("sep", ",").csv(source_file)

# Converter a coluna 'total' para inteiro
df = df.withColumn("total", col("total").cast(IntegerType()))

# Imprimir o esquema
df.printSchema()

# Transformar os nomes para maiúsculas
df = df.withColumn("nome", upper(col("nome")))

# Contar o número de linhas
print(f"Total de linhas: {df.count()}")

# Contar nomes agrupados por ano e sexo, ordenando pelo ano mais recente
df_grouped = df.groupBy("ano", "sexo").agg(count("nome").alias("total_nomes")).orderBy(desc("ano"))
df_grouped.show()

# Nome feminino com mais registros e o ano correspondente
nome_feminino = (
    df.filter(col("sexo") == "F")
    .groupBy("nome", "ano")
    .agg(F.sum("total").alias("total_ocorrencias"))
    .orderBy(F.desc("total_ocorrencias"))
    .first()
)
print(f"Nome feminino com mais registros: {nome_feminino}")

# Nome masculino com mais registros e o ano correspondente
nome_masculino = (
    df.filter(col("sexo") == "M")
    .groupBy("nome", "ano")
    .agg(F.sum("total").alias("total_ocorrencias"))
    .orderBy(F.desc("total_ocorrencias"))
    .first()
)
print(f"Nome masculino com mais registros: {nome_masculino}")

# Total de registros por ano (primeiras 10 linhas, ordenado por ano crescente)
df_totais_ano = (
    df.groupBy("ano")
    .agg(
        F.sum(when(col("sexo") == "F", col("total")).otherwise(0)).alias("total_feminino"),
        F.sum(when(col("sexo") == "M", col("total")).otherwise(0)).alias("total_masculino")
    )
    .orderBy("ano", ascending=True)
    .limit(10)
)
df_totais_ano.show()

# Selecionar as primeiras 10 linhas do DataFrame ordenado por ano
linhas_10 = df.orderBy(col("ano").asc()).limit(10)
linhas_10.show()

# Salvar o DataFrame com valores de nomes em MAIÚSCULO no S3
df.write.mode("overwrite").partitionBy("sexo", "ano").format("json").save(target_path)

job.commit()
