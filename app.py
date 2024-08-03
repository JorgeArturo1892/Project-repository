import pandas as pd
import plotly_express as px
import streamlit as st

cars_df = pd.read_csv('vehicles_us.csv')  # leer los datos de los vehículos
# creación de una casilla de verifiación
hist_check = st.checkbox('Construir histograma')
st.header('Exploración gráfica de datos de los anuncios para la venta de vehículos')
st.write('En esta aplicación podremos encontrar dos gráficas para la visualización de datos de nuestros vehículos en venta')

if hist_check:  # hacer click en la casilla
    # encabezado
    st.header('Consulta de datos de vehículos')
    # escribir un mensaje
    st.write('Creación de un histograma para nuestro conjunto de datos de anuncios de venta de vehículos con base en la columna odómetro')

    # creación de un gráfico de tipo histograma
    fig = px.histogram(cars_df, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# creación de una segunda casilla de verificación
disp_check = st.checkbox('Construir gráfico de dispersión')

if disp_check:  # hacer click en la segunda casilla
    # encabezado
    st.header('Nueva visualización de datos')
    # escribir nuevo mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos del anuncio de venta de vehículos')

    # creación del gráfico
    # creación de un gráfico de dispersión
    fig = px.scatter(cars_df, x="odometer", y="price")
    # crear gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
