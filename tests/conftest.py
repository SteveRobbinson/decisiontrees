import pandas as pd
from forest import config
import pytest
from forest.data_preprocessing import preprocess

@pytest.fixture
def preprocessed_df():
    df = preprocess(
    config.test_path,
    config.get_features,
    config.dummies,
    config.drop_list
    )
    
    return df

