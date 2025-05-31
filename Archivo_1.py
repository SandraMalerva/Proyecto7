import streamlit as st
import pandas as pd
import plotly.express as px
data_car = pd.read_csv(
    'D:\\Huawei Share\\Screenshot\\TRIPLE TEN\\visual studio\\Sprint7\\Proyecto7\\vehicles_us.csv')
st.header('Analisis de datos de Vehículos')

hist_button = st.button('Construir un histograma')
if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(data_car, x="odometer",
                       title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir un gráfico de dispersíon")
if scatter_button:
    st.write("Gráfico de dispersión: Relación entre odómetro y precio")
    fig = px.scatter(data_car, x="odometer", y="price", title="Relación  entre kilometraje y precio", labels={
                     "odometer": "kilometraje", "price": "Precio USD"}, opacity=0.6)
    st.plotly_chart(fig, use_container_width=True)
