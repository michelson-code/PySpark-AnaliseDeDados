from pyspark.sql.types import *
from pyspark.sql.functions import * 
from pyspark.sql import SparkSession


#import os
#os.environ["JAVA_HOME"] = "C:/Program Files/Eclipse Adoptium/jdk-17.0.16.8-hotspot"


spark = SparkSession.builder.appName("exemplo").getOrCreate()
df = spark.read.csv('data_science_job_posts_2025.csv', header=True, inferSchema=True)

'''This file contains 944 job postings related to Data Science roles across different 
companies. The dataset includes 13 columns covering job details, company information, 
and required skills.'''

df.show(5)

df.printSchema() # ver os tipos das colunas

# saber o numero de linhas 

print(df.count()) # 944 linhas


# verificar dados nulos

'''for coluna in df.columns:
    print(coluna, df.filter(df[coluna].isNull()).count())'''


# Contar vagas por cargo
df.groupBy('job_title').count().show()


# Split seguro na coluna salary
df2 = df.withColumn('salary_split', split(col('salary'), '-'))

# salary_min = valor esquerdo se houver faixa, 0 se só houver um valor
df2 = df2.withColumn(
    'salary_min',
    when(
        size(col('salary_split')) > 1,
        regexp_replace(col('salary_split').getItem(0), r'[^0-9.]', '').cast('float')
    ).otherwise(
        0.0
    )
)

# salary_max = valor direito se houver faixa, valor único se não houver
df2 = df2.withColumn(
    'salary_max',
    when(
        size(col('salary_split')) > 1,
        regexp_replace(col('salary_split').getItem(1), r'[^0-9.]', '').cast('float')
    ).otherwise(
        regexp_replace(col('salary_split').getItem(0), r'[^0-9.]', '').cast('float')
    )
)

# Corrige o caso de salary_min None para 0.0
df2 = df2.withColumn('salary_min', when(col('salary_min').isNull(), 0.0).otherwise(col('salary_min')))

# Visualizar salários tratados
df2.select("salary", "salary_min", "salary_max").show(truncate=False)

# Agrupar por profissão e calcular média salarial (da faixa)
df2.groupBy("job_title").agg(
    avg((col("salary_min") + col("salary_max")) / 2).alias("avg_salary")
).show(truncate=False)  # Você pode ordenar ou filtrar se quiser!
