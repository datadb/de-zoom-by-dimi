my homework answers

Q1.
- `--rm`

Q2.

0.42.0

Q3.
15612


both those:

SELECT COUNT(CAST(lpep_pickup_datetime AS DATE))
FROM
	green_taxi_trips g
WHERE
	CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
	AND
	CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18';


SELECT COUNT(CAST(lpep_dropoff_datetime AS DATE))
FROM
	green_taxi_trips g
WHERE
	CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
	AND
	CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18';

gave the same result

ALSO this:

SELECT
	CAST(lpep_pickup_datetime AS DATE),
	CAST(lpep_dropoff_datetime AS DATE),
	COUNT(*)
FROM
	green_taxi_trips g
WHERE
	CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
	AND
	CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18'
GROUP BY
	CAST(lpep_pickup_datetime AS DATE),
	CAST(lpep_dropoff_datetime AS DATE);

----------

Q4

SELECT
	CAST(lpep_pickup_datetime AS DATE),
	MAX(trip_distance)
FROM
	green_taxi_trips g
GROUP BY
	CAST(lpep_pickup_datetime AS DATE)
ORDER BY
	MAX(trip_distance) DESC;

# gave me 2019-09-26 as the result with trip distance 341.64