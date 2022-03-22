from airflow import DAG
from datetime import datetime, timedelta
# from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator


# initialising the default ags for DAG
default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2022, 3, 21),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG('Airflow_assignment',
          default_args=default_args,
          schedule_interval='@daily',
          template_searchpath=['/usr/local/airflow/sql_files'],
          catchup=False)

# t1 = PythonOperator(task_id='store_data_in_csv', python_callable=data_processing, dag=dag)

# Using PostgresOperator to create the table with same columns in csv file
t1 = PostgresOperator(task_id='create_postgres_table', postgres_conn_id='postgres_conn', sql="create_table.sql", dag=dag)

# Using PostgresOperator to insert the data from csv file into the postgres table
t2 = PostgresOperator(task_id='insert_into_table', postgres_conn_id='postgres_conn', sql="insert_into_table.sql", dag=dag)



t1 >> t2
