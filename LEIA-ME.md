# PySpark – Análise de vagas de Data Science

Repositório para estudos de **PySpark** usando um dataset de 944 vagas de trabalho em Data Science, com foco em leitura, limpeza e análise de dados em ambiente distribuído.[file:23]  

## Objetivos

- Criar uma `SparkSession` e ler arquivos CSV com `header` e `inferSchema`.
- Explorar o schema, contagem de linhas e presença de nulos.
- Tratar a coluna de salário (faixas salariais: mínimo e máximo).
- Calcular métricas como número de vagas por cargo e média salarial por cargo.[file:23]  

## Arquivos principais

- `data/data_science_job_posts_2025.csv`: dataset original de vagas.  
- `src/jobs_analysis.py`: script principal que:
  - lê o arquivo de dados;
  - mostra uma amostra (`show(5)`) e o schema (`printSchema()`);
  - conta o número de registros;
  - agrupa por `job_title` e conta vagas;
  - cria `salary_min` e `salary_max` a partir da coluna `salary`;
  - calcula `avg_salary` por cargo usando a média da faixa salarial.[file:23]  

## Como executar

1. Instale as dependências:
   ```
   pip install pyspark
   ```
2. Garanta que o arquivo `data_science_job_posts_2025.csv` está em `data/`.
3. Execute o script:
   ```
   python src/jobs_analysis.py
   ```

Será aberta uma sessão Spark, o dataset será lido e as principais estatísticas e agregações serão exibidas diretamente no console.[file:23]  

## Licença

Este projeto está licenciado sob os termos da licença MIT.
```
