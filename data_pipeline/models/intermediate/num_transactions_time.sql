{% set dimensions_full = ['sender_account', 'receiver_account', 'device_hash', 'ip_address'] %}
with staging_data as (
  select * from {{ ref('stg_transactions') }}
),

windows_computed as (
  select
    * 
    {% for dim in dimensions_full %}
      {% for i in range (var('time_frames')|length) %}
        , count(*) over(
          partition by {{ dim }}
          order by timestamp
          range between interval '{{ var('time_frames')[i] }}' preceding and current row
        ) as {{ dim.split('_')[0] }}_num_trx_{{ var('time_suffix')[i] }}
      {% endfor %}
    {% endfor %}
    from staging_data
  )

select * from windows_computed


