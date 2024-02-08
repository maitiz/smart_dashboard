import pandas as pd
import numpy as np

def add_light_intensity(df_food):
    np.random.seed(42)
    df_food['light_intensity'] = np.where(df_food['Timestamp'].dt.hour.between(9, 17),
                                          np.random.randint(290, 311, size=len(df_food)),
                                          np.random.randint(22, 56, size=len(df_food)))
    return df_food
