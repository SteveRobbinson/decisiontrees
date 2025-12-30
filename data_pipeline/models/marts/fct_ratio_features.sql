{% set time_suffix =  ['1h', '24h'] %}

with transaction_details as (
  select * from {{ ref('int_sum_amount') }}
),

transaction_details2 as (
  select * from {{ ref('int_count_trx') }}
),

joined_data as (
  select
    t1.*,
     {{ dbt_utils.star(from=ref('int_count_trx'), except=["transaction_id"], quote_identifiers=False) }}
  from transaction_details t1
  left join transaction_details2 t2
    on t1.transaction_id = t2.transaction_id
),

ratio_features as (
  select
    transaction_id,

    {# Obliczam jaki procent miesięcznych wydtków stanowi dana transakcja #}
    coalesce((amount / nullif(sender_mean_trx_30d, 0)), 1) as trx_sum_sender_ratio_30d
    
    {# Obliczam stosunek liczby transakcji w oknie 30d stanowi liczba transakcji w krótszych oknach #}
    {% for dim in var('dimension') %}
      {%- for i in range(time_suffix|length) -%}
      
        , ({{ dim }}_num_trx_{{ time_suffix[i] }} / {{ dim }}_num_trx_30d)
        as trx_count_{{ dim }}_ratio_{{ time_suffix[i] }}

      {% endfor %}
    {% endfor %}
  from joined_data
)

select * from ratio_features

