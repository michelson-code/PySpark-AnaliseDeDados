Para o README do GitHub, é melhor **não** deixar o texto inteiro dentro de caixa de código, só os trechos que são comandos ou código Python.[1]

Um ajuste bom seria:

```markdown
# PySpark – Análise de vagas de Data Science

Repositório para estudos de **PySpark** usando um dataset de 944 vagas de trabalho em Data Science, com foco em leitura, limpeza e análise de dados em ambiente distribuído.[file:23]  

## Objetivos

- Praticar criação de `SparkSession` e leitura de CSV com `header` e `inferSchema`.
- Explorar o schema, contagem de linhas e presença de nulos.
- Tratar a coluna de salário (faixas salariais, mínimo e máximo).
- Calcular métricas como número de vagas por cargo e média salarial por cargo.[file:23]  

## Arquivos principais

- `src/jobs_analysis.py`: script principal que:
  - lê o arquivo `data_science_job_posts_2025.csv`;
  - mostra amostra de linhas (`show(5)`) e o schema (`printSchema()`);
  - conta o número de registros;
  - agrupa por `job_title` e conta vagas;
  - cria colunas `salary_min` e `salary_max` e calcula `avg_salary` por cargo.[file:23]  

## Como executar

1. Instale o PySpark:
   ```
   pip install pyspark
   ```
2. Coloque o arquivo `data_science_job_posts_2025.csv` na pasta `data/`.
3. Execute o script:
   ```
   python src/jobs_analysis.py
   ```
```

Ou seja:  
- Títulos, listas e explicações em **Markdown normal**.  
- Apenas os comandos (`pip install`, `python ...`) dentro de blocos de código com ```bash``````python```

[1](https://www.codecademy.com/article/choosing-an-open-source-license)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/107546863/06234d71-a03b-4136-aa2d-a79ae68672fa/data_science_job_posts_2025.csv)
[3](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/107546863/9b12d7f5-f6eb-474b-b0a6-f07f69a9c72b/first_main.py)
