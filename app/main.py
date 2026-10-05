from fastapi import FastAPI, UploadFile
from app.checks import count_duplicates
import pandas as pd

app = FastAPI()

@app.post("/datasets")
def upload_dataset(file: UploadFile):
    df = pd.read_csv(file.file)
    rows, columns = df.shape
    missing = df.isna().sum().to_dict()
    return {
        "filename": file.filename,
        "rows": rows,
        "columns": columns,
        "missing" : missing,
        "duplicates": count_duplicates(df)
    }