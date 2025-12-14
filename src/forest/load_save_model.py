import pickle
from pathlib import Path

def save_model(
    model,
    config: dict,
    feature_names: list[str],
    path: str | Path
):
    
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    info = {
        'model': model,
        'config': config,
        'feature_names': feature_names
    }

    with open(path, 'wb') as f:
        pickle.dump(info, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_model(path: str | Path):
    with open(path, 'rb') as f:
        info = pickle.load(f)
    return info
