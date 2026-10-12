import streamlit as st
import folium
from streamlit_folium import st_folium

def mostrar_mapa():
    mapa=folium.Map(location=[-18.0146,-70.2536],zoom_start=9)
    st_folium(mapa,width=900,height=500)
