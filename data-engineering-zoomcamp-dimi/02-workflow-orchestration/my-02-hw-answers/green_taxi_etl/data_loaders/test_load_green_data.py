import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
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

        # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download'
    months = ["10", "11", "12"]
    filepaths = [url + '/green' + f"/green_tripdata_2020-{month}" + ".csv.gz" for month in months ]

    df = pd.DataFrame()
    data = []
    
    for filepath in filepaths:
        data.append(pd.read_csv(filepath, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates))
    df = pd.concat(data)
    print(df.shape)
    
    return df