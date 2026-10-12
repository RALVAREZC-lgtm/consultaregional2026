import streamlit as st
import pandas as pd
from pathlib import Path

def mostrar_consultas():
    st.header('Consulta de Mesas')
    ruta=Path('data/Maestro_EMR2026.xlsx')
    if ruta.exists():
        df=pd.read_excel(ruta)
        st.dataframe(df.head(100))
    else:
        st.warning('Copie Maestro_EMR2026.xlsx en la carpeta data')
