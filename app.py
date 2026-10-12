import streamlit as st
from dashboard import mostrar_dashboard
from consultas import mostrar_consultas
from incidencias import mostrar_incidencias
from resultados import mostrar_resultados
from mapas import mostrar_mapa

st.set_page_config(page_title="CONSULTA ELECTORAL - REGIONAL 2026",layout="wide")
st.title("CONSULTA ELECTORAL - REGIONAL 2026")
st.subheader("Centro de Comando Electoral Regional 2026 - Ahora Nación")
menu=st.sidebar.selectbox('Modulo',['Dashboard','Consulta de Mesas','Mapa','Incidencias','Resultados'])
if menu=='Dashboard': mostrar_dashboard()
elif menu=='Consulta de Mesas': mostrar_consultas()
elif menu=='Mapa': mostrar_mapa()
elif menu=='Incidencias': mostrar_incidencias()
elif menu=='Resultados': mostrar_resultados()
