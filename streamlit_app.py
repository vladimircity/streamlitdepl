import streamlit as st
from pandas import read_csv
from http.client import HTTPSConnection
from urllib.parse import quote_plus

conn = HTTPSConnection('docs.google.com')

goods = read_csv('price.csv', decimal=',')[['Артикул', 'Назва', 'Ціна']]

custom_product = 'Ввести вручну...'
custom_manager = '\+'
PRODUCTS = ['', custom_product] + goods['Назва'].values.tolist()

# Display Title and Description
st.header('Кузов-Центр')

MANAGERS = ['Віталій', 'Сергій', 'Тарас', custom_manager]

manager = st.radio('Менеджер:', MANAGERS, index=None, horizontal=True)
if manager == custom_manager:
    manager = st.text_input('Введіть менеджера:', key='manager_key')

product = st.selectbox('Товар:', options=PRODUCTS, key='product_key')
if product == custom_product:
    product = st.text_input('Введіть назву товару:')

price = st.text_input(label='Ціна', key='price_key')
price = int(price) if price else price

if 'quantity_key' not in st.session_state:
    st.session_state.quantity_key = 1  # Default value 1
quantity = st.number_input("Кількість", min_value=1, key='quantity_key')

customer = st.text_input(label='Клієнт')
notes = st.text_input(label='Нотатки')


def send_form():
    articul, base_price = get_product_info(product)
    total = price * quantity
    payload = f'entry.1975053655={manager}&entry.901466373={articul}&entry.401979653={product}&entry.276639414={base_price}&entry.1723905293={price}&entry.1073455884={quantity}&entry.1287285077={total}&entry.455948029={customer}&entry.665447278={notes}'
    payload = quote_plus(payload, safe=';/?:@&=+$,')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'COMPASS=spreadsheet_forms=CjIACWuJV7difwhCJlB853IBzNNy6fk2P9dFVjzUI3ZbRv8jL57Lvx7ZhuZHfu-rbN_ySBC3otOuBhpDAAlriVf80MSDJXDJrjynCZ1yTSYU8lKLJxAYDscCzpBkSaPz-Yhum8gQZbNgvEy9j3hD6YwPKJIbVWQYpd4s_tSivg==; S=spreadsheet_forms=OCpyNGOUFsbvKah3eh_93EjrDJhMOf24xlT7uYKYlDA; NID=511=kAtrWXMgZWzRWGyTSoOkvaCh1ap0WiRhqMzMUmA3oUXZNff0eC3ZX0qxlKXmdtCUWqts80zpigaMhtaG0QplApVh1TWO6TfyqwPykf1mviBFT920A9VDkS9PcBmFEGA1klHIAG0eB2vTuvXPYySSJyZda3eEACGEAVK6PJRUyaI',
    }

    conn.request(
        'POST',
        '/forms/u/0/d/e/1FAIpQLSdVmF4ylckGN6fi0TIYI_CM-akggUd3-VHl7IZHP8y2sJ85Yg/formResponse',
        payload,
        headers,
    )

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
    button = st.button(
        'Внести', on_click=send_form, use_container_width=False, type='primary'
    )
    st.write('')
    st.session_state.success = True

st.write("Подивитись всі  [ЗАМОВЛЕННЯ](https://docs.google.com/spreadsheets/d/1ThyJ0uPa3UNB1Yh1jh6EKIP2OutjFPX2F-GTypyBNYM/edit#gid=139450348)")
    

def get_product_info(product):
    articul = ''
    base_price = ''
    add_df = goods.loc[goods['Назва'] == product]

    if len(add_df):
        add_dict = add_df.reset_index().to_dict()
        articul = add_dict['Артикул'][0]
        base_price = add_dict['Ціна'][0]

    return articul, base_price
    
