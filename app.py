import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv(
    '~/proyectos/proyecto_sprint_5/notebooks/vehicles_us.csv')

print(car_data.head(5))
