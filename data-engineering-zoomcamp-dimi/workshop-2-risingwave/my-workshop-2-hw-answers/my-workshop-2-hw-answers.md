# My Homework Solutions

## Question 1

```sql
CREATE MATERIALIZED VIEW trip_times AS 
WITH t AS (
    SELECT 
        zpu.Zone AS pickup_taxi_zone, 
        zdo.Zone AS dropoff_taxi_zone, 
        trip_data.tpep_pickup_datetime, 
        trip_data.tpep_dropoff_datetime, 
        trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime AS trip_time 
    FROM 
        trip_data 
        JOIN taxi_zone AS zpu ON trip_data.pulocationid = zpu.location_id 
        JOIN taxi_zone AS zdo ON trip_data.dolocationid = zdo.location_id
    ) 
SELECT 
    pickup_taxi_zone, 
    dropoff_taxi_zone, 
    MIN(trip_time) AS min_trip_time, 
    MAX(trip_time) AS max_trip_time, 
    AVG(trip_time) AS avg_trip_time 
FROM t 
GROUP BY 
    pickup_taxi_zone, 
    dropoff_taxi_zone;
```

```sql
SELECT
    pickup_taxi_zone,
    dropoff_taxi_zone,
    avg_trip_time
FROM trip_times
WHERE avg_trip_time = (SELECT MAX(avg_trip_time) FROM trip_times);

--  pickup_taxi_zone | dropoff_taxi_zone | avg_trip_time 
-- ------------------+-------------------+---------------
--  Yorkville East   | Steinway          | 23:59:33
--  (1 row)

```

## Question 2

```sql
CREATE MATERIALIZED VIEW trip_times_count AS 
    WITH t AS (
        SELECT 
            zpu.Zone AS pickup_taxi_zone, 
            zdo.Zone AS dropoff_taxi_zone, 
            trip_data.tpep_pickup_datetime, 
            trip_data.tpep_dropoff_datetime, 
            trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime AS trip_time 
        FROM 
            trip_data 
            JOIN taxi_zone AS zpu ON trip_data.pulocationid = zpu.location_id 
            JOIN taxi_zone AS zdo ON trip_data.dolocationid = zdo.location_id
    ) 
    SELECT 
        pickup_taxi_zone, 
        dropoff_taxi_zone, 
        AVG(trip_time) AS avg_trip_time,
        COUNT(*) AS trips_count
    FROM 
        t 
    GROUP BY 
        pickup_taxi_zone, 
        dropoff_taxi_zone
    ORDER BY avg_trip_time DESC;
```
```sql
SELECT
    pickup_taxi_zone,
    dropoff_taxi_zone,
    avg_trip_time,
    trips_count
FROM trip_times_count
LIMIT 1;

-- pickup_taxi_zone | dropoff_taxi_zone | avg_trip_time | trips_count 
--------------------+-------------------+---------------+-------------
-- Yorkville East   | Steinway          | 23:59:33      |           1
-- (1 row)

```
## Question 3

```sql
CREATE MATERIALIZED VIEW top_busiest_cities AS
WITH t AS (
    SELECT MAX(tpep_pickup_datetime) AS latest_pickup_time
    FROM trip_data
    )
SELECT 
    zpu.Zone AS pickup_taxi_zone,
    COUNT(zpu.Zone) as count_trips
FROM t, trip_data
JOIN taxi_zone AS zpu ON trip_data.pulocationid = zpu.location_id 
JOIN taxi_zone AS zdo ON trip_data.dolocationid = zdo.location_id
WHERE 
    trip_data.tpep_pickup_datetime > (t.latest_pickup_time - INTERVAL '17' HOUR)
GROUP BY 
    pickup_taxi_zone
ORDER BY 
    count_trips DESC
LIMIT 3;
```
```sql
SELECT * from top_busiest_cities;

--  pickup_taxi_zone   | count_trips 
-----------------------+-------------
-- LaGuardia Airport   |          19
-- JFK Airport         |          17
-- Lincoln Square East |          17
-- (3 rows)

```