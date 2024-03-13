import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # Se leen los datos


st.header('Proyecto final sprint 5: Curso de análisis de datos')

st.subheader('Vista de los datos')

# -- Create three columns
col1, col2, col3 = st.columns([5, 5, 20])
# -- Put the image in the middle column
# - Commented out here so that the file will run without having the image downloaded
# with col2:
# st.image("streamlit.png", width=200)
# -- Put the title in the last column
with col3:
    st.title("Vehículos")
# -- We use the first column here as a dummy to add a space to the left

# -- Get the user input
year_col, col, type_col = st.columns([5, 5, 5])

with year_col:
    year_choice = st.slider(
        "Elige el año del modelo del vehículo:",
        min_value=1908,
        max_value=2019,
        step=1,
        # value=2010,
    )

with type_col:
    type_choice = st.selectbox(
        "¿Qué tipo de vehículo quieres ver?",
        ("All", "bus", "convertible", "coupe", "hatchback", "mini-van",
         "offroad", "other", "pickup", "sedan", "SUV", "truck ", "wagon", "van"),
    )

# -- Apply the type filter
if type_choice == "All":
    filtered_df = car_data[(car_data.model_year == year_choice)]
else:
    filtered_df = car_data[(car_data.type == type_choice) &
                           (car_data.model_year == year_choice)]
# -- Apply the year filter given by the user
# filtered_df = car_data[(car_data.model_year == year_choice)]


st.table(filtered_df.sort_values(by='price').head(10))


st.subheader('Creación de gráficos')

# Se crea un botón para ahcer un histograma
hist_check = st.checkbox('Construir un histograma')

if hist_check:  # Seleccionar crea un histograma
    nested_button = st.button("Crear histograma")

    if nested_button:
        # Escribir un mensaje
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos.')
        # Crar un histograma
        histogram_odometer = px.histogram(car_data, x='odometer')
        # Mostrar un grafico Plotly interactivo.
        st.plotly_chart(histogram_odometer, use_container_width=True)

# Se crea un botón para hacer un gráfico de dispersión.
scatter_check = st.checkbox('Construir un gráfico de dispersión')

if scatter_check:  # Seleccionar crear un gráfico de dispersión
    nested_button = st.button('Crear gráfico de dispersión')

    if nested_button:
        # Escribir un mensaje
        st.write('Creación de un gráfico de dispersión.')

        # Crear gráfico de dispersión
        scatter_odo_price = px.scatter(car_data, x="odometer", y="price",
                                       title='Relación entre el precio y el recorrido de los vehículos.')

        # Mostrar un gráfico Plotly interactivo.
        st.plotly_chart(scatter_odo_price, use_container_width=True)

# Se crea un botón para hacer un gráfico de barras.
bar_check = st.checkbox('Construir gráfico de barras')

if bar_check:  # Seleccionar crear un gráfico de dispersión
    nested_button = st.button('Crear gráfico de barras')

    if nested_button:
        # Escribir un mensaje
        st.write('Creación de un gráfico de barras.')

        bar_graph = px.bar(car_data, x='type', y='price', color='fuel',
                           title='Gráfico de precios por tipo de vehículo y tipo de combustible.')
        st.plotly_chart(bar_graph, use_container_width=True)
