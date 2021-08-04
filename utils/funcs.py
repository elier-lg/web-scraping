from pathlib import Path

def ensure_folder(folder):
    Path(folder).mkdir(parents=True, exist_ok=True)  