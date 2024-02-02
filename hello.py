import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Vendor Management Portal")
st.markdown("Enter the details of the new vendor below.")

url = "https://docs.google.com/spreadsheets/d/1ThyJ0uPa3UNB1Yh1jh6EKIP2OutjFPX2F-GTypyBNYM/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[1, 2])
st.dataframe(data)