import streamlit as st
import pickle
import json
import numpy as np
import pandas as pd

# Load the trained model
with open('Benglore_House_Price_Prediction_Model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the columns used in the model
with open('columns.json', 'r') as f:
    data_columns = json.load(f)["data_columns"]
    
st.set_page_config(page_title="Bengaluru House Price Prediction", page_icon="🏠", layout="centered")
st.title("Bengaluru House Price Prediction")
st.write("This app predicts the price of a house in Bengaluru based on various features.")

locations = data_columns[3:] #1st 3 are numerical fearutes so we've left them.
location = st.selectbox("Select Location", locations)

sqft = st.number_input(
    "Total Area in Square Feet",
    min_value = 300,
    max_value = 30000,
    value = 1000,
    step = 10
)

bhk = st.number_input(
    "BHK",
    value=2,
    min_value=1,
    max_value=16
)
bath = st.number_input(
    "No. of Bathrooms",
    value=2,
    min_value=1,
    max_value=16
)

if st.button("Predict Price"):
    st.write('Button CLicked')