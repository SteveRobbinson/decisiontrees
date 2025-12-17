from forest.downsample_majority import downsample_majority 
from forest import config

def test_downsampling(df_preprocessed):
    
    df_downsampled = downsample_majority(df_preprocessed, config.num_samples_test)
    
    assert len(df_downsampled) < len(df_preprocessed)

    before = (df_preproccessed['is_fraud'] == True).sum()
    after = (df_downsampled['is_fraud'] == True).sum()
    assert before == after
