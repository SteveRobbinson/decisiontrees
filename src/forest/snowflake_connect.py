import snowflake.connector
from cryptography.hazmat.primitives import serialization
import os
from dotenv import load_dotenv
from forest.key_reader import read_key

load_dotenv()

def connect_to_snowflake(key_path: str):

    private_key = read_key(key_path)

    conn = snowflake.connector.connect(
        user = os.getenv('SNOWFLAKE_USER'),
        account = os.getenv('SNOWFLAKE_ACCOUNT'),
        private_key = private_key,
        warehouse = os.getenv('SNOWFLAKE_WAREHOUSE'),
        database= os.getenv('SNOWFLAKE_DATABASE'),
        schema= os.getenv('SNOWFLAKE_SCHEMA')
    )

    return conn

