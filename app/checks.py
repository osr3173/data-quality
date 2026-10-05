import pandas as pd

def count_duplicates(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())

def find_type_mismatches(df: pd.DataFrame) -> dict:
    result = {}
    for col in df.select_dtypes(include=['object','string']).columns:
        values = df[col].dropna()
        if len(values) == 0:
            continue
        converted = pd.to_numeric(values, errors = 'coerce')
        numeric_ratio = len(converted.dropna()) / len(values)
        if numeric_ratio > 0.5:
            result[col] = int(converted.isna().sum())
    return result