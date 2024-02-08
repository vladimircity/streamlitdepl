import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

goods = pd.read_csv('price.csv')[['Артикул', 'Назва', 'База']]

custom_product = "Ввести вручну..."
PRODUCTS = ['', custom_product] + goods['Назва'].values.tolist()

# Display Title and Description
st.title("Продажа Кузов Центр")

MANAGERS = ["Віталій", "Сергій", "Тарас",]

manager = st.selectbox("Менеджер*", options=MANAGERS, index=None)
product = st.selectbox("Товар*", options=PRODUCTS, key='product_key')
if product == custom_product: 
    product = st.text_input("Введіть назву товару:")

price = st.text_input(label="Ціна", key='price_key')


quantity = st.selectbox("Кількість", options=[1,2,3,4,5,6,7,8,9,10,11,12], index=0, key='quantity_key')
customer = st.text_input(label="Клієнт")
notes = st.text_area(label="Нотатки")

cols=st.columns(2)
with cols[0]:
    a = st.text_input('name')
with cols[1]:
    a = st.text_input('Year')

if not price:
    flag = True
else:
    flag = False

def reset():
    st.session_state.product_key = ''
    st.session_state.quantity_key = 1
    st.session_state.price_key = ''


button = st.button('Внести', on_click=reset)

if button:
    st.success('Товар Успішно внесено')

### Discover streamlit necessary fields control