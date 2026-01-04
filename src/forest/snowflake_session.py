from snowflake.snowpark import Session

def create_session(config: dict) -> Session:
    return Session.builder.configs(config).create()
