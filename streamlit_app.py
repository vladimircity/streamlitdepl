import streamlit as st
import gspread
from pandas import read_csv
from datetime import datetime


CREDENTIALS = {
        "type" : st.secrets["gcp_service_account"]["type"],
        "project_id" : st.secrets["gcp_service_account"]["project_id"],
        "private_key_id" : st.secrets["gcp_service_account"]["private_key_id"],
        "private_key" : st.secrets["gcp_service_account"]["private_key"],
        "client_email" : st.secrets["gcp_service_account"]["client_email"],
        "client_id" : st.secrets["gcp_service_account"]["client_id"],
        "auth_uri" : st.secrets["gcp_service_account"]["auth_uri"],
        "token_uri" : st.secrets["gcp_service_account"]["token_uri"],
        "auth_provider_x509_cert_url" : st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url" : st.secrets["gcp_service_account"]["client_x509_cert_url"],
    }


if 'gsheet' not in st.session_state:
    gclient = gspread.service_account_from_dict(CREDENTIALS)
    gwb = gclient.open('Kuzov Sales')
    gws = gwb.worksheet('Orders2')
    print('gws.id =', gws.id)
    st.session_state.gsheet = gws

goods = read_csv('price.csv')[['Артикул', 'Назва', 'База']]

custom_product = "Ввести вручну..."
custom_manager = "Інший"
PRODUCTS = ['', custom_product] + goods['Назва'].values.tolist()

# Display Title and Description
st.header("Кузов-Центр: створити замовлення")

MANAGERS = ["Віталій", "Сергій", "Тарас", "Інший"]

manager = st.radio("Менеджер:", MANAGERS, index=None, horizontal=True)
if manager == custom_manager: 
    manager = st.text_input("Введіть менеджера:", key='manager_key')


product = st.selectbox("Товар:", options=PRODUCTS, key='product_key')
if product == custom_product: 
    product = st.text_input("Введіть назву товару:")

price = st.text_input(label="Ціна", key='price_key')
price = int(price) if price else price
quantity = st.selectbox("Кількість", options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], index=0, key='quantity_key')
customer = st.text_input(label="Клієнт")
notes = st.text_input(label="Нотатки")
rate = st.radio(" ", ['👍', '👎'], index=0, horizontal=True)


def reset():
    values_list = [datetime.now().strftime("%d-%m-%Y %H:%M:%S"), manager, 13777, product, 50, price, quantity, customer, notes]
    save(values_list)
    st.session_state.product_key = ''
    st.session_state.price_key = ''
    st.session_state.quantity_key = 1


if not product or not manager:
    if 'success' not in st.session_state:
        st.session_state.success = False
        st.warning('Заповніть поля менеджер і товар')
    elif st.session_state.success:
        st.success('Товар успішно внесено')
        st.warning('Заповніть наступний товар')
    else:
        st.warning('Заповніть поля менеджер і товар')
else:
    button = st.button('Внести', on_click=reset, use_container_width=False, type='primary')
    st.write('')
    st.session_state.success = True


def save(values_list):
    print(values_list)
    st.session_state.gsheet.append_row(values_list, value_input_option='USER_ENTERED')
   


