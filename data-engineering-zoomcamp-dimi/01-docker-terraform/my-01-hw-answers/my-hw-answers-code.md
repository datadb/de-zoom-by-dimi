my homework answers code

# Q1.
docker run --help

# Q2.

docker run -it --entrypoint=bash python:3.9
pip list

# Q3.

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

# Q4.

SELECT
	CAST(lpep_pickup_datetime AS DATE),
	MAX(trip_distance)
FROM
	green_taxi_trips g
GROUP BY
	CAST(lpep_pickup_datetime AS DATE)
ORDER BY
	MAX(trip_distance) DESC;

# Q5.

SELECT
	SUM(total_amount),
	CAST(lpep_pickup_datetime AS DATE),
	zpu."Borough"
FROM
	green_taxi_trips g
	RIGHT JOIN zones zpu
		ON g."PULocationID" = zpu."LocationID"
WHERE
	CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
GROUP BY
	CAST(lpep_pickup_datetime AS DATE),
	zpu."Borough"
ORDER BY
	SUM(total_amount) DESC;

# Q6.

## one query
SELECT
	zpu."Zone",
	MAX(tip_amount) AS max_tip_amount,
	"DOLocationID"
FROM
	green_taxi_trips g
JOIN zones zpu
	ON g."PULocationID" = zpu."LocationID"
WHERE
	EXTRACT(MONTH FROM lpep_pickup_datetime)= 9 AND
	zpu."Zone" = 'Astoria'
GROUP BY
	zpu."Zone",
	"DOLocationID"
ORDER BY
	MAX(tip_amount) DESC
LIMIT 1;

## another query

SELECT
	"Zone"
FROM
	zones
WHERE
	"LocationID" = 132;

## alternative solution IN ONE query:

SELECT
	zpu2."Zone",
	MAX(tip_amount) AS max_tip_amount,
	"DOLocationID"
FROM
	green_taxi_trips g
JOIN zones zpu
	ON g."PULocationID" = zpu."LocationID"
JOIN zones zpu2
	ON g."DOLocationID" = zpu2."LocationID"
WHERE
	EXTRACT(MONTH FROM lpep_pickup_datetime)= 9 AND
	zpu."Zone" = 'Astoria'
GROUP BY
	zpu2."Zone",
	"DOLocationID"
ORDER BY
	MAX(tip_amount) DESC
LIMIT 1;

# Q7.

inserted the following in the variables.tf:

variable "credentials" {
  description = "My Credentials"
  default     = "/workspaces/de-zoom-by-dimi/data-engineering-zoomcamp-dimi/01-docker-terraform/terrademo/keys/my-creds.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "mydezoomcamp2024"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "europe-west1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "dimi_demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "my-dezoomcamp-2024-terra-bucket-by-dimidb-with-variables"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

AND THEN

terraform apply