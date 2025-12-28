# PySpark – Data Science Job Postings Analysis

Repository for **PySpark** practice using a dataset of 944 Data Science job postings, focusing on data loading, cleaning, and exploratory analysis in a distributed environment. 

## Goals

- Create a `SparkSession` and read CSV files with `header` and `inferSchema`.
- Explore the schema, row count, and potential missing data.
- Clean and parse the salary column (ranges: minimum and maximum).
- Compute metrics such as number of openings per job title and average salary per job title.[file:23]  

## Main files

- `data/data_science_job_posts_2025.csv`: original job postings dataset.  
- `src/jobs_analysis.py`: main script that:
  - reads the dataset;
  - shows a sample (`show(5)`) and the schema (`printSchema()`);
  - counts the number of records;
  - groups by `job_title` and counts the number of openings;
  - creates `salary_min` and `salary_max` from the `salary` column;
  - computes `avg_salary` per job title using the mean of the salary range.[file:23]  

## How to run

1. Install dependencies:
   ```
   pip install pyspark
   ```
2. Make sure `data_science_job_posts_2025.csv` is placed inside the `data/` folder.
3. Run the script:
   ```
   python src/jobs_analysis.py
   ```

This will start a Spark session, load the dataset, and print the main statistics and aggregations directly to the console.[file:23]  

## License

This project is licensed under the MIT License.
