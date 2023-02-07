import streamlit as st
# from gsheetsdb import connect

with st.form("my_form"):
   st.write("Inside the form")
   nombAp = st.text_input('Nombre y Apellido', 'Pedro Perez')
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, 
                "checkbox", checkbox_val,
                "nombre y apellido",nombAp)

st.write("Outside the form")
st.write('###', nombAp)
nombApF = '*'+nombAp+'*'
st.write(nombApF)

nucel, nilidxcel = 0, 0
nucel = st.text_input('Nro de gruposA','0')
nulidxcel = st.number_input('Nro de lideres X grupo', )
nulidTot = int(nucel) * nulidxcel
st.write('Total lideres = ', int(nulidTot))

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


