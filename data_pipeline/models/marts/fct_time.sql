with staging_data as (
  select * from {{ ref('stg_transactions') }}
),

time_features as (
  select
    day(timestamp) as day_of_month,
    month(timestamp) as month,
    hour(timestamp) as hour_of_day,
    dayofweekiso(timestamp) as day_of_week
  from staging_data
)
select *,
  case
    when day_of_week in (6, 7) then 1
    else 0
  end as is_weekend
from time_features
