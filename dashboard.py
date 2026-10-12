import streamlit as st

def mostrar_dashboard():
    c1,c2,c3,c4=st.columns(4)
    c1.metric('Mesas',1250)
    c2.metric('Personeros',1180)
    c3.metric('Incidencias',12)
    c4.metric('Locales',87)
