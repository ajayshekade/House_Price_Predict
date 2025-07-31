import streamlit as st
import pickle
import numpy as np

# Load model and columns
model = pickle.load(open("house_price_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.set_page_config(page_title="India House Price Predictor", layout="centered")

st.title("🏠 India House Price Predictor")
st.markdown("Enter the details below to estimate the house price:")

# Input fields
size = st.number_input("Size (in SqFt):", min_value=300, max_value=10000, value=1000, step=100)
bhk = st.selectbox("Number of BHKs:", [1, 2, 3, 4, 5])
location = st.selectbox("Location:", ["Mumbai", "Delhi", "Bangalore"])

# Create input vector based on trained columns
input_data = []

for col in columns:
    if col == "Size":
        input_data.append(size)
    elif col == "BHK":
        input_data.append(bhk)
    elif col.startswith("Location_"):
        loc_name = col.split("Location_")[1]
        input_data.append(1 if location == loc_name else 0)

# Predict and show result
if st.button("Predict Price"):
    prediction = model.predict([input_data])[0]
    st.success(f"💰 Estimated House Price: ₹ {round(prediction, 2)} Lakhs")
