import streamlit as st

nomyap = "Pedro Perez"
title = st.text_input('Nombre y Apellido', nomyap)
st.write('Su nombre y apellido es: ', title)

