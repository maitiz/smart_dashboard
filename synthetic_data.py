import pandas as pd
import numpy as np
import plotly.express as px


def generate_fig1(max_level, noise_scale):
    np.random.seed(42)
    time_index = pd.date_range(start='2023-05-24', end='2023-05-26', freq='H')
    base_levels = np.linspace(22, max_level, len(time_index))
    noise = np.random.normal(0, noise_scale, len(time_index))
    ammonia_levels = np.clip(base_levels + noise, 22, max_level)

    df_ammonia = pd.DataFrame({'Timestamp': time_index, 'Ammonia_Level': ammonia_levels})
    fig1 = px.line(df_ammonia, x='Timestamp', y='Ammonia_Level',
                   title=f'Ammonia Levels Over Time (Max {max_level})')
    return fig1
