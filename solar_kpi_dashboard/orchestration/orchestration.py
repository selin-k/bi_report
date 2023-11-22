# filename: solar_kpi_dashboard/orchestration/orchestration.py
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Import the necessary modules for the ETL tasks
from ..data_ingest.data_ingestion import DataIngestion
from ..data_curate.data_curation import DataCuration
from ..data_transformation.data_transformation import DataTransformation
from ..data_visualization.dashboard import Dashboard

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'solar_panel_kpi_dashboard',
    default_args=default_args,
    description='ETL pipeline for Solar Panel KPI Dashboard',
    schedule_interval=timedelta(days=1),
)

# Define the ETL tasks
ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=DataIngestion().ingest_data,
    dag=dag,
)

curate_task = PythonOperator(
    task_id='curate_data',
    python_callable=DataCuration().curate_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=DataTransformation().transform_data,
    dag=dag,
)

# Define a wrapper function for the visualization task
def visualize_wrapper():
    # Load the transformed data and calculate the KPIs
    dashboard_service = Dashboard()
    fact_table = dashboard_service.load_transformed_data()
    kpis = {'KPI Name': ['Total Energy Produced'], 'Value': [fact_table['energy_produced'].sum()]}
    # Create the visualizations
    dashboard_service.create_visualizations(kpis)

# Update the visualize_task to use the wrapper function
visualize_task = PythonOperator(
    task_id='create_visualizations',
    python_callable=visualize_wrapper,
    dag=dag,
)

# Set the task execution order
ingest_task >> curate_task >> transform_task >> visualize_task