-- Created a new GSC bucket and service account for week 03 homework
-- Created the external table in ny_taxi dataset
-- using the add button in Bigquery and loading data from the .parquet file in the new GCS bucket
-- Delesected "use cached results" in query settings

-- Check GREEN trip data
SELECT * FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_external limit 10;

-- Create a non partitioned GREEN table from external table -- this is materialized table
CREATE OR REPLACE TABLE mydezoomcamp2024.ny_taxi.green_taxidata_2022_non_partitioned AS 
SELECT *
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_external;

-- Q2 
SELECT COUNT (DISTINCT PULocationID)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_external

-- Q2
SELECT COUNT (DISTINCT PULocationID)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_non_partitioned

-- Q3
SELECT COUNT (DISTINCT fare_amount)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_non_partitioned
WHERE fare_amount = 0;

-- Q3 ALTERNATIVE
SELECT SUM(case when fare_amount = 0 then 1 else 0 end)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_non_partitioned;

-- Q4 -- Creating a partition and cluster table from external table GREEN
CREATE OR REPLACE TABLE mydezoomcamp2024.ny_taxi.green_taxidata_2022_partitioned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_external;

-- Q5 -- Querying the non partitioned table GREEN
-- estimate 12.82
SELECT DISTINCT(PULocationID)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_non_partitioned
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- Q5 -- Querying the partitioned + clustered table GREEN
-- estimate 1.12 MB
SELECT DISTINCT(PULocationID)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_partitioned_clustered
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- Q6 -- GCS Bucket

-- Q7 -- False

-- Q8 Materialized table non partitioned GREEN
-- estimate 0 Β
SELECT COUNT (*)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_non_partitioned

-- Q8 Materialized table partitioned and clustered GREEN
-- estimate 0 Β
SELECT COUNT (*)
FROM mydezoomcamp2024.ny_taxi.green_taxidata_2022_partitioned_clustered