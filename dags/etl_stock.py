
from src.config import CONN_URL, NEW_TABLE_NAME, ROOT_DIR, ticker
from datetime import datetime, timezone
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.utils.task_group import TaskGroup


from src.pop_data import populate_table
from src.create_table import create_table
from src.api_call import get_data

default_args = {
    "retries": 0,
    "start_date": days_ago(5),
    "depends_on_past": False,
    "wait_for_downstream": True,
}

with DAG(
    dag_id="stock-update",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    create_table_task = PythonOperator(
        task_id="create_table_task",
        python_callable=create_table,
        op_args=[CONN_URL, NEW_TABLE_NAME],
    )
    with TaskGroup(group_id=f"get_daily_data") as get_daily_data_task_group:
        for tick in ticker:
            call_api = PythonOperator(
                task_id=f"get_{tick}_daily_data",
                python_callable=get_data,
                op_args=[tick, ROOT_DIR],
                provide_context=True,
            )
    populate_table = PythonOperator(
        task_id="lleno_tabla",
        python_callable=populate_table,
        op_args=[NEW_TABLE_NAME, ROOT_DIR, CONN_URL],
    )



create_table_task >> get_daily_data_task_group >> populate_table
