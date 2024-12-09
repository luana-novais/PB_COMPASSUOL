import boto3
import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SQLContext
from awsglue.job import Job

# Configurações do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input', 'exit'])
sc = SparkContext()
glueContext = GlueContext(sc)
sqlContext = SQLContext(sc)

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['input']
target_path = args['exit']

# Carregar arquivos JSON
df_json = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="json"
)

df_json_spark = df_json.toDF()

df_json_spark.write.mode("overwrite").parquet(target_path)

job.commit()
