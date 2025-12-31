from pathlib import Path
import os
from dotenv import load_dotenv

base_dir = Path(__file__).parents[2]

load_dotenv()

connection_parameters = {
  "account": os.getenv('SNOWFLAKE_ACCOUNT'),
  "user": os.getenv('SNOWFLAKE_USER'),
  "password": os.getenv('SNOWFLAKE_PASSWORD'),
  "role": os.getenv('SNOWFLAKE_ROLE'),
  "warehouse": os.getenv('SNOWFLAKE_WAREHOUSE'),
  "database": os.getenv('SNOWFLAKE_DATABASE'),
  "schema": os.getenv('SNOWFLAKE_SCHEMA')
}

