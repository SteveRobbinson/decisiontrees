SELECT
  CAST(transaction_id as VARCHAR) as transaction_id,
  CAST(timestamp as datetime) as timestamp,
  CAST(sender_account as VARCHAR) as sender_account,
  CAST(receiver_account as VARCHAR) as receiver_account,
  CAST(amount as FLOAT) as amount,
  CAST(transaction_type as VARCHAR) as transaction_type,
  CAST(merchant_category as VARCHAR) as merchant_category,
  CAST(location as VARCHAR) as location,
  CAST(device_used as VARCHAR) as device_used,
  CAST(is_fraud as BOOLEAN) as is_fraud,
  CAST(fraud_type as VARCHAR) as fraud_type,
  CAST(time_since_last_transaction as FLOAT) as time_since_last_transaction,
  CAST(spending_deviation_score as FLOAT) as spending_deviation_score,
  CAST(velocity_score as INTEGER) as velocity_score,
  CAST(geo_anomaly_score as FLOAT) as geo_anomaly_score,
  CAST(payment_channel as VARCHAR) as payment_channel,
  CAST(ip_address as VARCHAR) as ip_address,
  CAST(device_hash as VARCHAR) as device_hash
FROM
  {{ source('snowflake_raw', 'LOCAL_DATA') }}
