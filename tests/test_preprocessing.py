import pandas as pd
from forest import config
from forest.data_preprocessing import preprocess

def test_preprocessing():
    df = preprocess(
    config.test_path,
    config.get_features,
    config.dummies,
    config.drop_list
    )

    for col in config.drop_list:
        assert col not in df.columns

    assert df.isnull().sum().sum() == 0
