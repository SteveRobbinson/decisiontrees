from snowflake.snowpark import Session, DataFrame
import pandas as pd

def create_sets(connection: Session,
                table_name: str,
                size_sets: list[float]) -> tuple[DataFrame, ...]:
    
    df = connection.table(table_name)
    
    datasets = df.random_split(size_sets, 42)
    names = ['train', 'val', 'test']

    for data, name in zip(datasets, names):
        data.write.mode('overwrite').save_as_table(name + "_table")

    return tuple(datasets)
