{{
    config(
        materialized='view'
    )
}}

with 

tripdata as (

    select * from {{ source('staging', 'fhv_tripdata') }}
    WHERE EXTRACT(YEAR FROM pickup_datetime) = 2019
),

renamed as (

    select
        dispatching_base_num,
        pickup_datetime,
        dropoff_datetime,
        PUlocationID,
        DOlocationID,
        sr_flag,
        affiliated_base_number
    from tripdata

)

select * from renamed

-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}