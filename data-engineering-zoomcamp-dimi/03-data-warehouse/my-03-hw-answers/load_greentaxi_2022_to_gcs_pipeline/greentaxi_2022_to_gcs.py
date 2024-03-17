import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# Replace with the location of your service account key JSON file.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/mydezoomcamp2024-5506e111ebc2.json'

bucket_name = '03-warehouse-dimi'
object_key = 'green_taxi_2022.parquet'
where = f'{bucket_name}/{object_key}'

@data_exporter
def export_data(data, *args, **kwargs):
    table = pa.Table.from_pandas(data, preserve_index=False)
    gcs = pa.fs.GcsFileSystem()

    pq.write_table(
        table,
        where,

        # Convert integer columns in Epoch milliseconds
        # to Timestamp columns in microseconds ('us') so
        # they can be loaded into BigQuery with the right
        # data type
        coerce_timestamps='us',

        filesystem=gcs
    )