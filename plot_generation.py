import plotly.express as px

def plot_data(df, option, show_moving_avg, title):
    fig = px.line(df, x='Timestamp', y=option, title=f'Time Series Plot of {title}')
    if show_moving_avg:
        df['MA'] = df[option].rolling(window=3).mean()
        fig.add_scatter(x=df['Timestamp'], y=df['MA'], mode='lines', name='3-hour MA', line=dict(color='red', dash='dash'))
    return fig

def plot_light_intensity(df):
    return px.line(df, x='Timestamp', y='light_intensity', title='Light Intensity Over Time')
