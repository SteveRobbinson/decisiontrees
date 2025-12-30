with staging_data as (
  select * from {{ ref('stg_transactions') }}
),

age_user as (
  select
    transaction_id,
    datediff(day, first_value(timestamp) over(
    partition by sender_account
    order by timestamp
    range between unbounded preceding and current row),
    timestamp
    )  as age_of_sender_account
  from staging_data
)

select * from age_user
    
 
