with base as (
  select * from {{ ref('int_count_trx') }}
)

select * from base
where
{% for dim in var('dimension') %}
  (
    {% for i in range(var('time_suffix')|length - 1) %}
      {{ dim }}_num_trx_{{ var('time_suffix')[i] }} > {{ dim }}_num_trx_{{ var('time_suffix')[i+1] }}
      {% if not loop.last %} or {% endif %}
    {% endfor %}
  )
  {% if not loop.last %} or {% endif %}
{% endfor %}
