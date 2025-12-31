from snowflake.snowpark import Session

def load_data(config: dict) -> Session:
    return Session.builder.configs(config).create()
