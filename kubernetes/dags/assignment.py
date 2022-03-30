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
          template_searchpath=['/mnt/airflow/dags'],
          catchup=False)

# t1 = PythonOperator(task_id='store_data_in_csv', python_callable=data_processing, dag=dag)
t1 = PostgresOperator(task_id="create_new_table",postgres_conn_id='postgres_conn',sql="create_new_table.sql", dag=dag)

t1