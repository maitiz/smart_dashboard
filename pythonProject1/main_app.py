import streamlit as st
from data_preparation import load_data
from light_intensity_data import add_light_intensity
from plot_generation import plot_data, plot_light_intensity
from synthetic_data import generate_fig1
from column_mapping import column_mapping




# Load and prepare data
df_food, df_water = load_data()
df_food = add_light_intensity(df_food)

def main():
    st.title("Smart Cage system, peritonite experiment - Dashboard")

    # Food Data Visualization
    expander_food = st.expander("Food Data Visualization")
    with expander_food:
        option_food = st.selectbox('Choose the treatment for food:', options=list(column_mapping.keys()), format_func=lambda x: column_mapping[x], key='food_expander')
        show_moving_avg_food = st.checkbox('Show 3-hour Moving Average', key='mv_avg_food_expander')
        fig_food = plot_data(df_food, option_food, show_moving_avg_food, 'Food')
        st.plotly_chart(fig_food, use_container_width=True)

    # Water Data Visualization
    expander_water = st.expander("Water Data Visualization")
    with expander_water:
        option_water = st.selectbox('Choose the treatment for water:', options=list(column_mapping.keys()), format_func=lambda x: column_mapping[x], key='water_expander')
        show_moving_avg_water = st.checkbox('Show 3-hour Moving Average', key='mv_avg_water_expander')
        fig_water = plot_data(df_water, option_water, show_moving_avg_water, 'Water')
        st.plotly_chart(fig_water, use_container_width=True)

    # Light Intensity Visualization
    expander_light = st.expander("Light Intensity Over Time")
    with expander_light:
        fig_light_intensity = plot_light_intensity(df_food)
        st.plotly_chart(fig_light_intensity, use_container_width=True)

    # Synthetic Ammonia Levels Visualization
    expander_ammonia = st.expander("Ammonia Levels Over Time")
    with expander_ammonia:
        cage_selector = st.selectbox("Select Cage for Ammonia Level Visualization", ["Cage 1", "Cage 2", "Cage 3"], key='cage_selector_expander')
        cage_params = {
            "Cage 1": {"max_level": 50, "noise_scale": 5},
            "Cage 2": {"max_level": 35, "noise_scale": 2},
            "Cage 3": {"max_level": 60, "noise_scale": 1}
        }
        fig_ammonia = generate_fig1(max_level=cage_params[cage_selector]["max_level"], noise_scale=cage_params[cage_selector]["noise_scale"])
        st.plotly_chart(fig_ammonia, use_container_width=True)

st.markdown(
    """
    <style>
    .reportview-container {
        background: #1E1E1E;
        color: white;
    }
    .sidebar .sidebar-content {
        background: #1E1E1E;
    }
    </style>
    """,
    unsafe_allow_html=True
)




if __name__ == "__main__":
    main()
