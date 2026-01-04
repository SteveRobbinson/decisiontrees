from snowflake.snowpark.functions import sproc
from snowflake.snowpark import Session
import forest.config as config
from forest.snowflake_session import create_session
from forest.dataset_split import create_sets
from forest.train_fraud_detection import train_model
from forest.snowflake_connect import connect_to_snowflake
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to snowflake
conn = connect_to_snowflake(os.getenv('SNOWFLAKE_PRIVATE_KEY_PATH'))


# Create snowflake session
snowflake_session = create_session({'connection': conn})


# Load and create train and validation sets
train, val, test = create_sets(snowflake_session,
                               config.get_config(snowflake_session)['preproccessed_table'],
                               config.get_config(snowflake_session)['size_sets']
                               )


# Initialize Stored Procedure
@sproc(
    name = config.get_config(snowflake_session)['stored_procedure']['name'],
    packages = config.get_config(snowflake_session)['stored_procedure']['packages'],
    is_permanent = False,
    stage_location = config.get_config(snowflake_session)['stage_location'],
    replace = True,
    imports=['config.py', 'train_fraud_detection.py']
)

# Train fraud model
def run_training(connection: Session) -> str:
    
    import pandas as pd
    import joblib
    import lightgbm as lgb
    import config
    from train_fraud_detection import train_model

    train_model(connection,
                'train',
                'val',
                config.get_config(connection)['fraud_label'],
                config.get_config(connection)['stage_location']
                )

    return 'Chyba pykło'

print(snowflake_session.call(config.get_config(snowflake_session)['stored_procedure']['name']))
