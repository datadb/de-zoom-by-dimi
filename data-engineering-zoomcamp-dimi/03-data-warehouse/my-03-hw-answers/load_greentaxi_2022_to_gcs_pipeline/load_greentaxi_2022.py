import io
import pandas as pd
import requests
#import pyarrow as pa
import pyarrow.parquet as pq

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    service = 'green' # service = kwargs['service']
    year = '2022' #year = kwargs['year']
    print(f'loading {service} taxi data for the year {year}\n')

    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    data_frames = []

    for i in range(12):
        month = f"{i+1:02d}"
        file_name = f"{service}_tripdata_{year}-{month}.parquet"
        request_url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}'
        print(f'request url: {request_url}')
        try:
            response = requests.get(request_url)
            response.raise_for_status()  # Raises HTTPError for bad requests
            data = io.BytesIO(response.content)
            # Read Parquet file into an Arrow Table
            table = pq.read_table(data)
            # Convert Arrow Table to Pandas DataFrame
            df = table.to_pandas()
            # Parse date columns
            df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
            df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])
            
            df = df.astype(taxi_dtypes)

            data_frames.append(df)
            print(f"Parquet loaded: {file_name}")
        except requests.HTTPError as e:
            print(f"HTTP Error: {e}")
            # Optionally, handle the error (e.g., by breaking the loop or re-trying)

    # Concatenate all dataframes
    combined_df = pd.concat(data_frames, ignore_index=True)
    print(combined_df.dtypes)
    return combined_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'