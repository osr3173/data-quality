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

def find_outliers(df: pd.DataFrame) -> dict:
    result = {}
    for col in df.columns:
        values = df[col].dropna()
        if len(values) == 0:
            continue
        converted = pd.to_numeric(values, errors = 'coerce')
        numbers = converted.dropna()
        if len(numbers) / len(values) <= 0.5:
            continue
        q1 = numbers.quantile(0.25)
        q3 = numbers.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        count = ((numbers < lower) | (numbers > upper)).sum()
        if count > 0:
            result[col] = int(count)
    return result
