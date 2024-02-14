import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.write(st.secrets["gcp_service_account"]['type'])
