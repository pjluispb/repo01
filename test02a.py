# importing pandas as pd
import pandas as pd
import streamlit as st
# ----------------------------------------
st.write('Lectura del csv')
newurl = 'https://raw.githubusercontent.com/pjluispb/miscvs/main/Prondanmin23.csv'
df = pd.read_csv(newurl, index_col='cedula')
st.write(df)
try:
    first = df.loc[5125570]
except:
    st.write('cedula no existe')
else:
    st.write('cedula existe')
    st.write(first)

 

