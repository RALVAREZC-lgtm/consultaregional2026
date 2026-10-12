import streamlit as st

def mostrar_incidencias():
    st.header('Registro de Incidencias')
    st.text_input('Mesa')
    st.selectbox('Tipo',['Falta Personero','Observacion','Otro'])
    st.text_area('Descripcion')
    st.file_uploader('Foto')
    if st.button('Guardar Incidencia'):
        st.success('Incidencia registrada')
