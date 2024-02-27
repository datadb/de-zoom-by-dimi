CREATE OR REPLACE EXTERNAL TABLE `mydezoomcamp2024.trips_data_all.external_fhv_tripdata`
  (
    dispatching_base_num STRING,
    pickup_datetime INT64,
    dropOff_datetime INT64,
    PUlocationID INT64,
    DOlocationID INT64,
    SR_Flag INT64,
    Affiliated_base_number STRING
  )
OPTIONS (
  format = 'parquet',
  uris = ['gs://04-analytics-dimi/fhv/fhv_tripdata_2019-*.parquet']
);

CREATE OR REPLACE TABLE `mydezoomcamp2024.trips_data_all.fhv_tripdata` (
  dispatching_base_num STRING,
  pickup_datetime TIMESTAMP,
  dropoff_datetime TIMESTAMP,
  PUlocationID INT64,
  DOlocationID INT64,
  SR_Flag INT64,
  Affiliated_base_number STRING
) AS (
SELECT 
    dispatching_base_num,
    TIMESTAMP_MICROS(CAST(pickup_datetime / 1000 AS INT64)) AS pickup_datetime,
    TIMESTAMP_MICROS(CAST(dropoff_datetime / 1000 AS INT64)) AS dropoff_datetime,
    PUlocationID,
    DOlocationID,
    SR_Flag,
    Affiliated_base_number
FROM `mydezoomcamp2024.trips_data_all.external_fhv_tripdata`
);

SELECT COUNT(*)
FROM `mydezoomcamp2024.prod.fact_fhv_trips`