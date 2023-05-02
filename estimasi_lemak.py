import pickle
import streamlit as st

model = pickle.load(open('estimasi_lemak.sav', 'rb'))

st.title('Estimasi Jumlah Lemak Di Menu Burger King')

Calories = st.number_input('Input Jumlah Kalori')
Saturated_Fat = st.number_input('Input Jumlah Lemak Jenuh (g)')
Trans_Fat = st.number_input('Input Total Lemak Trans (g)')
Total_Carb = st.number_input('Input Total Karbohidrat (g)')
Sugars = st.number_input('Input Jumlah Gula (g)')
Cholesterol = st.number_input('Input Jumlah Kolesterol (g)')

predict = ''

if st.button('Estimasi Lemak'):
    predict = model.predict(
        [[Calories, Saturated_Fat, Trans_Fat, Total_Carb, Sugars, Cholesterol]]
        )
    st.write ('Estimasi Jumlah Lemak di setiap Menu Burger King : ', predict)