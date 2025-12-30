with staging_data as (
  select * from {{ ref('stg_transactions') }}
),

is_receiver_known as (
  select
    transaction_id,
    case
      when count(*) over(
        partition by sender_account, receiver_account
        order by timestamp
        rows between unbounded preceding and 1 preceding
      ) > 0 then 1
      else 0
    end as is_receiver_known
  from staging_data
)

select * from is_receiver_known
