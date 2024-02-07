import streamlit as st

if 'something' not in st.session_state:
    st.session_state.something = ''

st.title("Welcome to compute Request")
input_value = st.text_input('Something', placeholder='Please enter a value')
if input_value == 'quit':
    st.error("You can't quit right now")

elif input_value != '' and input_value != 'quit':
    st.session_state.something = input_value
    st.write(f'Last submission: {st.session_state.something}')