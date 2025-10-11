import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Size_sqft': [850, 950, 1100, 1200, 1350, 1450, 1600, 1750, 1800, 1900,
                  2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
                  3000, 3100, 3200, 3400, 3600, 3800, 4000, 4200, 4500, 4800],
    'Bedrooms': [2, 2, 2, 3, 3, 3, 3, 3, 3, 3,
                 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
                 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],
    'Age': [15, 14, 13, 12, 10, 9, 8, 7, 7, 6,
            5, 5, 4, 4, 4, 3, 3, 2, 2, 2,
            2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Price': [175000, 190000, 210000, 225000, 240000, 250000, 260000, 270000, 275000, 280000,
              290000, 295000, 305000, 310000, 320000, 330000, 340000, 350000, 360000, 365000,
              375000, 385000, 390000, 400000, 420000, 440000, 460000, 480000, 500000, 520000]
}

data = pd.DataFrame(data)

st.title("House Price Predictor")

size = st.selectbox(label="Size of house (sqft)", options=data['Size_sqft'])

bed = st.slider(label="Number of bedrooms", max_value=5, min_value=2)

age = st.slider(label="Age of house", max_value=15, min_value=2)

if st.button('Estimate'):
    reg=LinearRegression()
    reg.fit(X=data[['Size_sqft', 'Bedrooms', 'Age']], y=data['Price'])

    price = reg.predict([[size, bed, age]])
    st.success(f"Estimated price: ${price[0]:,.2f}")