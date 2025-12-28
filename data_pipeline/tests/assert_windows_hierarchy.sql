with base as (
  select * from {{ ref('num_transactions_time') }}
),

select * from base
where
{% for dim in var('dimension') %}  
  (
    {{ dim }}_num_trx_{{ var('time_suffix')[0] }} > {{ dim }}_num_trx_{{ var('time_suffix')[1] }}
    {{ dim }}_num_trx_{{ var('time_suffix')[1] }} > {{ dim }}_num_trx_{{ var('time_suffix')[2] }}
    {{ dim }}_num_trx_{{ var('time_suffix')[2] }} > {{ dim }}_num_trx_{{ var('time_suffix')[3] }}
  )
  {% if not loop.last %} or {% endif %}
{% endfor %}

