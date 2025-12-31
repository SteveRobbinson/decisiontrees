{% set features = ['fct_age_of_user', 'fct_is_receiver_known', 'fct_location_frequency', 'fct_ratio_features', 'fct_time'] %}
{% set col_to_drop = ['sender_account', 'receiver_account', 'device_hash', 'ip_address', 'fraud_type', 'merchant_category', 'location', 'device_used', 'payment_channel'] %}

with staging_data as (
  select
    {{ dbt_utils.star(from = ref('stg_transactions'), except =col_to_drop, quote_identifiers = False) }}
  from {{ ref('stg_transactions') }}
),

{% for feat in features %}
{{ feat.split('_')[1:]|join('_') }}_table as (
  select * from {{ ref(feat) }}
),
{% endfor %}

final_features as (
  select
    source.*,
    {% for feat in features %}
      t{{ loop.index }}.* exclude(transaction_id)
      {%- if not loop.last %}, {% endif %}
    {% endfor %}
  from staging_data source

  {% for  feat in features -%}
    left join {{ feat.split('_')[1:]|join('_') }}_table t{{ loop.index }}
      on source.transaction_id = t{{ loop.index }}.transaction_id
  {% endfor %}
  order by timestamp
)

select * from final_features    
