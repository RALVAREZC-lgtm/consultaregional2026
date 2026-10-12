import streamlit as st

def mostrar_resultados():
    st.header('Resultados')
    st.text_input('Mesa')
    st.number_input('Ahora Nacion',0)
    st.number_input('Oponente',0)
    if st.button('Guardar Resultado'):
        st.success('Resultado registrado')
