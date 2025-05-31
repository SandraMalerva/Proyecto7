import streamlit as st
import pandas as pd
import plotly.express as px

data_car = pd.read_csv(
    'D:\\Huawei Share\\Screenshot\\TRIPLE TEN\\visual studio\\Sprint7\\Proyecto7\\vehicles_us.csv')

st.header('Análisis de Venta de Vehículos')


select_condition = st.selectbox(
    "Selecciona condición del véhiculo:", data_car['condition'].dropna().unique())
filtered_condition = data_car[data_car['condition'] == select_condition]
st.write(f"Mostrando véhiculos en condición: **{select_condition}**")
st.dataframe(filtered_condition)


filtered_condition = data_car[data_car['condition'] == select_condition]
fig_price_hist = px.histogram(filtered_condition, x='price', nbins=50,
                              title=f'Distribución de Precios por Condicion: {select_condition}', labels={'price': 'Precio USD'}, color_discrete_sequence=['#ff7f0e'])
st.plotly_chart(fig_price_hist, use_container_width=True)


st.sidebar.header("Gráficos")

button_dis = st.sidebar.button('Precio vs Año del Modelo')
show_hist = st.sidebar.checkbox('Histograma del odómetro')
show_scatter = st.sidebar.checkbox('Mostrar dispersión: odómetro vs precio')
show_bar = st.sidebar.checkbox('Gráfico de barras relativo por tipo')
if button_dis:
    st.write('Relación entre Año del Modelo y Precio')
    fig = px.scatter(data_car, x="model_year", y="price",  labels={
                     "model_year": "Año del Modelo", "price": "Precio"}, opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)

if show_hist:
    st.write('Histograma del odómetro')
    fig = px.histogram(data_car, x="odometer",
                       title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

if show_scatter:
    st.write("Dispersión: Kilometraje vs Precio")
    fig = px.scatter(data_car, x="odometer", y="price", title="Kilometraje y Precio", labels={
        "odometer": "kilometraje", "price": "Precio USD"}, opacity=0.6, color_discrete_sequence=["#45ec32"])
    st.plotly_chart(fig, use_container_width=True)

if show_bar:
    grouped = data_car.groupby(
        ['model', 'type']).size().reset_index(name='count')
    fig = px.bar(grouped, x='model', y='count', color='type', barmode='relative', title='Distribución Relativa de Tipos de Véhiculo por Modelo',
                 labels={'model': 'Modelo', 'count': 'Cantidad'})
    st.plotly_chart(fig, use_container_width=True)
