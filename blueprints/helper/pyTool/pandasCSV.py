import pandas as pd

def getSpiritual():
    df = pd.read_csv('./data/spiritual.csv')
    return df

resp = getSpiritual()
print(f"DataFrame = {resp}")