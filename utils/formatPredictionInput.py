import pandas as pd
from common import model_columns

def formatPredictionInput(request):
    return pd.DataFrame({col: [request[col]] for col in model_columns})
