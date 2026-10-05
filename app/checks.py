import pandas as pd

def count_duplicates(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())