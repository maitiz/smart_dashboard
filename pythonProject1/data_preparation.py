import pandas as pd

def load_data():
    df_food = pd.read_csv('hourly_food.csv').fillna(0)
    df_water = pd.read_csv('hourly_water.csv').fillna(0)
    df_food['Timestamp'] = pd.to_datetime(df_food['Timestamp'])
    return df_food, df_water
