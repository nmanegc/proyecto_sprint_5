import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # Se leen los datos

st.header('Proyecto final sprint 5: Curso de análisis de datos')

# Se crea un botónv para ahcer un histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer click
    # Escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos.')

    # Crar un histograma
    histogram_odometer = px.histogram(car_data, x='odometer')

    # Mostrar un grafico Plotly interactivo.
    st.plotly_chart(histogram_odometer, use_container_width=True)

# Se crea un botón para hacer un gráfico de dispersión.
disp_button = st.button('Crea un gráfico de dispersión')

if hist_button:  # Al hacer click
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión.')

    # Crar un histograma
    scatter_odo_price = px.scatter(car_data, x="odometer", y="price",
                                   title='Relación entre el precio y el recorrido de los vehículos.')

    # Mostrar un grafico Plotly interactivo.
    st.plotly_chart(scatter_odo_price, use_container_width=True)
