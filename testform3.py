import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

goods = pd.read_csv('price.csv')[['Артикул', 'Назва', 'База']]

custom_product = "Ввести вручну..."
custom_manager = "Інший"
PRODUCTS = ['', custom_product] + goods['Назва'].values.tolist()

# Display Title and Description
st.header("Кузов-Центр: створити замовлення")


MANAGERS = ["Віталій", "Сергій", "Тарас", "Інший"]

# manager = st.selectbox("Менеджер*", options=MANAGERS, index=None)

manager = st.radio("Менеджер:", MANAGERS, index=None, horizontal=True)
if manager == custom_manager: 
    manager = st.text_input("Введіть менеджера:")

product = st.selectbox("Товар:", options=PRODUCTS, key='product_key')
if product == custom_product: 
    product = st.text_input("Введіть назву товару:")

price = st.text_input(label="Ціна", key='price_key')
quantity = st.selectbox("Кількість", options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], index=0, key='quantity_key')
customer = st.text_input(label="Клієнт")
notes = st.text_input(label="Нотатки")


def reset():
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
    st.session_state.success = True


### Створити таблицю замовлень