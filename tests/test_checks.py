from pathlib import Path
import pandas as pd
from app.checks import count_duplicates, find_type_mismatches, find_outliers

DATA = Path(__file__).parent/"data"/"orders_with_defects.csv"

def load_df():
    return pd.read_csv(DATA)

def test_count_duplicates():
    df = load_df()
    assert count_duplicates(df) == 1