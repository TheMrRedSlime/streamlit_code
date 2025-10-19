import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

st.title("Breast Cancer Risk Detector")
st.subheader("An app used to detect whether a tumor is non-cancerous or cancerous")

st.header("Enter the measurements for your report:")
mean_radius = st.number_input(label="Mean radious (size of nuclei)", min_value=0.0)
mean_texture = st.number_input(label="Mean texture (variation texture)", min_value=0.0)
mean_perimeter = st.number_input(label="Mean perimeter (boundary length)", min_value=0.0)
mean_area = st.number_input(label="Mean Area (area of nuclei)",min_value=0.0)

x,y = load_breast_cancer(return_X_y=True)
reg=LogisticRegression()
X_train,X_test,Y_train,Y_test=train_test_split(x, y, test_size=0.2, random_state=21)
reg.fit(X_train,Y_train)

table={
    "Mean Radius": mean_radius,
    "Mean Texture": mean_texture,
    "Mean Perimeter": mean_perimeter,
    "Mean Area": mean_area
}

st.dataframe(table)


if st.button("Click here to predict"):
    st.header("Prediction result")
    result=reg.predict([[mean_area, mean_texture, mean_perimeter, mean_area] + [0]*(x.shape[1]-4)])
    if result == 1:
        st.success("Non-Cancerous!")
    else:
        st.error("Cancerous")