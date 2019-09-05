import pandas as pd
import pdb
from common import model_columns

def formatPredictionInput(request):
    df = {}
    for col in model_columns:
        df[col] = [request[col]]
    return pd.DataFrame(df)
