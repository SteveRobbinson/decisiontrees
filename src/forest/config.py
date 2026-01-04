from pathlib import Path
import os
import lightgbm as lgb

# Bezpiecznik dla importu dotenv
try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

results = {}

def get_config(session=None) -> dict:

    if session is not None:

        return {
            'snowflake_info': {
                "SNOWFLAKE_USER": session.get_current_user(),
                "SNOWFLAKE_ACCOUNT": session.get_current_account() ,
                "SNOWFLAKE_WAREHOUSE": session.get_current_warehouse(),
                "SNOWFLAKE_DATABASE": session.get_current_database(),
                "SNOWFLAKE_SCHEMA": session.get_current_schema()
            },
            
            **config
        }
        
    from dotenv import load_dotenv
    load_dotenv()

    return {
        'connection_parameters': {
            "account": os.getenv('SNOWFLAKE_ACCOUNT'),
            "user": os.getenv('SNOWFLAKE_USER'),
            "role": os.getenv('SNOWFLAKE_ROLE'),
            "warehouse": os.getenv('SNOWFLAKE_WAREHOUSE'),
            "database": os.getenv('SNOWFLAKE_DATABASE'),
            "schema": os.getenv('SNOWFLAKE_SCHEMA')
        },

        **config
    }

        
config = {
        'preproccessed_table': 'the_great_join',

        'size_sets': [0.8, 0.1, 0.1],

        'lightgbm_config': {
            'objective': 'binary',
            'metric': 'auc',
            'boosting_type': 'gbdt',
            'learning_rate': 0.01, 
            'num_leaves': 31,     
            'max_depth': -1,      
            'min_data_in_leaf': 2000, 
            'feature_fraction': 0.9,
            'is_unbalance': True,
            'bagging_fraction': 0.8,
            'bagging_freq': 5,
            'seed': 42,
            'verbosity': -1,
            'boost_from_average': True
        },

        'stage_location': '@ml_stage',

        'fraud_label': 'IS_FRAUD',

        'num_boost_round': 10,

        'callbacks': [
            lgb.log_evaluation(20),
            lgb.early_stopping(50),
            lgb.record_evaluation(results)
        ],

        'stored_procedure': {
                'name': 'train_fraud_detection',
                'packages': ['lightgbm',
                             'joblib',
                             'pandas',
                             'snowflake-snowpark-python'
                             ]
        }
}
