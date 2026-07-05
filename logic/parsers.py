import pandas as pd
from io import BytesIO


def read_xlsx(file: BytesIO) -> pd.DataFrame:
    df = pd.read_excel(file)
    return df