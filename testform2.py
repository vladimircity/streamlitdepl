import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing vendors data
existing_data = conn.read(worksheet="Orders", usecols=list(range(12)), ttl=5)
existing_data = existing_data.dropna(how="all")

print(existing_data)

# # Add the new vendor data to the existing data
# updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

# Update Google Sheets with the new vendor data
conn.update(worksheet="Orders2", data=existing_data)

