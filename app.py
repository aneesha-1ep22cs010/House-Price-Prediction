import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(page_title="House Price Estimator", layout="centered")

# Load the model you just exported in image_3aa613d.png
model = joblib.load('house_model.pkl')

st.title("🏡 Ames House Price Predictor")
st.write("Adjust the parameters below to estimate the house value.")

# Sidebar for additional info
st.sidebar.header("About the Model")
st.sidebar.info("This model uses Linear Regression trained on the Ames Housing dataset with a 79% accuracy rate.")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    area = st.number_input("Living Area (Sq Ft)", value=1500)
with col2:
    garage = st.number_input("Garage Size (Cars)", 0, 5, 2)
    basement = st.number_input("Total Basement Area (Sq Ft)", value=1000)

# Prediction Logic
if st.button("Predict Price"):
    features = pd.DataFrame([[qual, area, garage, basement]], 
                            columns=['Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Total Bsmt SF'])
    prediction = model.predict(features)[0]
    
    st.markdown("---")
    st.subheader(f"Estimated Price: **${prediction:,.2f}**")
    st.balloons()