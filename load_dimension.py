from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 sql_insert_query="",
                 insert_mode="append",  # خيارين: append أو delete-load
                 *args, **kwargs):
        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_insert_query = sql_insert_query
        self.insert_mode = insert_mode

    def execute(self, context):
        self.log.info(f"Connecting to Redshift: {self.redshift_conn_id}")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        if self.insert_mode == "delete-load":
            self.log.info(f"Deleting data from dimension table {self.table}")
            redshift.run(f"DELETE FROM {self.table}")

        self.log.info(f"Inserting data into dimension table {self.table}")
        insert_sql = f"INSERT INTO {self.table} {self.sql_insert_query}"
        redshift.run(insert_sql)
        self.log.info(f"Finished inserting data into {self.table}")
