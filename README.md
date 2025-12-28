# [EN] PySpark – Data Science Job Postings Analysis

Repository for **PySpark** practice using a dataset of 944 Data Science job postings, focusing on data loading, cleaning, and exploratory analysis in a distributed environment. 

## Goals

- Create a `SparkSession` and read CSV files with `header` and `inferSchema`.
- Explore the schema, row count, and potential missing data.
- Clean and parse the salary column (ranges: minimum and maximum).
- Compute metrics such as number of openings per job title and average salary per job title.

## Main files

- `data/data_science_job_posts_2025.csv`: original job postings dataset.  
- `src/jobs_analysis.py`: main script that:
  - reads the dataset;
  - shows a sample (`show(5)`) and the schema (`printSchema()`);
  - counts the number of records;
  - groups by `job_title` and counts the number of openings;
  - creates `salary_min` and `salary_max` from the `salary` column;
  - computes `avg_salary` per job title using the mean of the salary range.

## How to run

1. Install dependencies:
   ```bash
   pip install pyspark
   ```
2. Make sure `data_science_job_posts_2025.csv` is placed inside the `data/` folder.
3. Run the script:
   ```bash
   python src/jobs_analysis.py
   ```

This will start a Spark session, load the dataset, and print the main statistics and aggregations directly to the console.

## License

This project is licensed under the MIT License.

# [PT-BR] PySpark – Análise de vagas de Data Science

Repositório para estudos de **PySpark** usando um dataset de 944 vagas de trabalho em Data Science, com foco em leitura, limpeza e análise de dados em ambiente distribuído.

## Objetivos

- Criar uma `SparkSession` e ler arquivos CSV com `header` e `inferSchema`.
- Explorar o schema, contagem de linhas e presença de nulos.
- Tratar a coluna de salário (faixas salariais: mínimo e máximo).
- Calcular métricas como número de vagas por cargo e média salarial por cargo.

## Arquivos principais

- `data/data_science_job_posts_2025.csv`: dataset original de vagas.  
- `src/jobs_analysis.py`: script principal que:
  - lê o arquivo de dados;
  - mostra uma amostra (`show(5)`) e o schema (`printSchema()`);
  - conta o número de registros;
  - agrupa por `job_title` e conta vagas;
  - cria `salary_min` e `salary_max` a partir da coluna `salary`;
  - calcula `avg_salary` por cargo usando a média da faixa salarial. 

## Como executar

1. Instale as dependências:
   ```bash
   pip install pyspark
   ```
2. Garanta que o arquivo `data_science_job_posts_2025.csv` está em `data/`.
3. Execute o script:
   ```bash
   python src/jobs_analysis.py
   ```

Será aberta uma sessão Spark, o dataset será lido e as principais estatísticas e agregações serão exibidas diretamente no console.

## Licença

Este projeto está licenciado sob os termos da licença MIT.


