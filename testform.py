import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

goods = pd.read_csv('price.csv')[['Артикул', 'Назва', 'База']]

custom_product = "Ввести вручну..."
PRODUCTS = [custom_product] + goods['Назва'].values.tolist()

# Display Title and Description
st.title("Продажа Кузов Центр")
# st.markdown("Enter the details of the new vendor below.")

# # Establishing a Google Sheets connection
# conn = st.connection("gsheets", type=GSheetsConnection)

# # Fetch existing vendors data
# existing_data = conn.read(worksheet="Vendors", usecols=list(range(6)), ttl=5)
# existing_data = existing_data.dropna(how="all")

# List of Business Types and Products
MANAGERS = [
    "Віталій",
    "Сергій",
    "Тарас",
]



# Onboarding New Vendor Form
with st.form(key="vendor_form"):

    manager = st.selectbox("Менеджер*", options=MANAGERS, index=None)

    placeholder_for_product = st.empty()
    placeholder_for_optional_text = st.empty()
    
    price = st.text_input(label="Ціна")
    quantity = st.selectbox("Кількість", options=[1,2,3,4,5,6,7,8,9,10,11,12], index=0)
    customer = st.text_input(label="Клієнт")
    notes = st.text_area(label="Нотатки")

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit Vendor Details")

    if submit_button:
        st.warning("Ensure all mandatory fields are filled.")
        st.stop()
    
# Create selectbox
with placeholder_for_product:
    product = st.selectbox("Товар*", options=PRODUCTS, index=None)


# Create text input for user entry
with placeholder_for_optional_text:
    if product == custom_product: 
        product = st.text_input("Введіть назву товару:")


# add_df = goods.loc[goods['Назва'] == 'VW Passat B8 2016 накладка туманки правая']
# add_df['Ціна'] = 250
# print(add_df)

    # # If the submit button is pressed
    # if submit_button:
    #     # Check if all mandatory fields are filled
    #     if not company_name or not business_type:
    #         st.warning("Ensure all mandatory fields are filled.")
    #         st.stop()
    #     elif existing_data["CompanyName"].str.contains(company_name).any():
    #         st.warning("A vendor with this company name already exists.")
    #         st.stop()
    #     else:
    #         # Create a new row of vendor data
    #         # TODO Create matching columns in gsheet
    #         vendor_data = pd.DataFrame(
    #             [
    #                 {
    #                     "CompanyName": company_name,
    #                     "BusinessType": business_type,
    #                     "Products": ", ".join(products),
    #                     "YearsInBusiness": years_in_business,
    #                     "OnboardingDate": onboarding_date.strftime("%Y-%m-%d"),
    #                     "AdditionalInfo": additional_info,
    #                 }
    #             ]
    #         )

    #         # Add the new vendor data to the existing data
    #         updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

    #         # Update Google Sheets with the new vendor data
    #         conn.update(worksheet="Vendors", data=updated_df)

    #         st.success("Vendor details successfully submitted!")
