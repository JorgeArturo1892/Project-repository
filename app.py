import pandas as pd
import plotly_express as px
import streamlit as st

cars_df = pd.read_csv('vehicles_us.csv')
fig = px.histogram(cars_df, x="odometer")  # crear un histograma
fig.show()  # crear gráfico de dispersión
