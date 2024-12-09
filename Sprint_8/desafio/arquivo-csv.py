import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import regexp_replace, lower, trim, col, floor

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input', 'exit'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

current_date = datetime.now()
year = current_date.year
month = current_date.month
day = current_date.day

source_file = args['input']
target_path = f"{args['exit']}/{year}/{month:02d}/{day:02d}/"

df = spark.read.option("header", "true").option("sep", "|").csv(source_file)

df = df.fillna({'notaMedia': 0, 'numeroVotos': 0, 'nomeArtista': 'Desconhecido'})

df = df.withColumn("notaMedia", df["notaMedia"].cast("float"))

df = df.withColumn("anoLancamento", regexp_replace("anoLancamento", r"\\N", ""))

df = df.withColumn("anoLancamento", df["anoLancamento"].cast("int"))

df = df.withColumn("tituloPincipal", regexp_replace("tituloPincipal", "[^a-zA-Z0-9\s]", ""))

df = df.withColumn("tituloPincipal", trim(col("tituloPincipal")))

df = df.withColumn("personagem", trim(col("personagem")))

df_filtrado = df.filter(df['genero'].contains('Sci-Fi'))

df_somente_sci_fi = df_filtrado.filter(df['genero'] == 'Sci-Fi') \
    .select("id", "tituloOriginal", "anoLancamento", "genero", "notaMedia", "numeroVotos", "nomeArtista", "personagem")

df_sci_fi_com_outros = df_filtrado.filter(df['genero'].contains('Sci-Fi') & (df['genero'] != 'Sci-Fi')) \
    .select("id", "tituloOriginal", "anoLancamento", "genero", "notaMedia", "numeroVotos", "nomeArtista", "personagem")

df_somente_sci_fi.write.mode("overwrite").parquet(target_path + "/somente_sci_fi")
df_sci_fi_com_outros.write.mode("overwrite").parquet(target_path + "/sci_fi_com_outros")

job.commit()