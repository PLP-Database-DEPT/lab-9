import dlt
from dlt.sources.sql_database import sql_database

def load_tables_customers_and_payments():
    source = sql_database().with_resources("customers", "payments")

    pipeline = dlt.pipeline(
        pipeline_name="data_pipeline",
        destination="duckdb",
        dataset_name="sales"
    )

    load_info = pipeline.run(source)
    print(load_info)

if __name__ == '__main__':
    load_tables_customers_and_payments()
