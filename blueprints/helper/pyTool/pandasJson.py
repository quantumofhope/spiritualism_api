import pandas as pd

def getChurches():
    df = pd.read_json('./data/rec2.json')
    return df


resp = getChurches()
print(f"DataFrame = {resp}")