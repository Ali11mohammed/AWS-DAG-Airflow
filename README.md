# Final Project - Data Pipelines with Airflow

### Project Description
This project builds an automated data pipeline using Apache Airflow.  
The pipeline stages event and song data from S3 to Redshift, processes the data into a star schema, and performs data quality checks.

---

### Project Architecture
- Source data: **S3** (`s3://udacity-dend/`)
- Staging and Final tables: **Amazon Redshift**
- Workflow orchestration: **Apache Airflow**

---

### How It Works
1. **Begin_execution**: Dummy start task.
2. **Stage_events** and **Stage_songs**:  
   - Copy event and song datasets from **S3** to **Redshift** staging tables.
3. **Load_songplays_fact_table**:  
   - Load the `songplays` fact table from the staging tables.
4. **Load Dimension Tables**:  
   - Load the dimension tables: `users`, `songs`, `artists`, and `time`.
5. **Run_data_quality_checks**:  
   - Verify that tables are not empty.
6. **Stop_execution**: Dummy end task.

---

### Operators Implemented
- `StageToRedshiftOperator`: Load data from S3 into Redshift staging tables.
- `LoadFactOperator`: Load data into the fact table.
- `LoadDimensionOperator`: Load data into dimension tables.
- `DataQualityOperator`: Perform data quality checks on Redshift tables.

---

### Execution
- DAG is scheduled to run **every hour** (`@hourly`).
- Manual trigger available for testing.

---
