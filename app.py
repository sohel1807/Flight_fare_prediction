import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import pickle

# Load trained model
data = pickle.load(open("main.pkl", "rb"))

st.title("✈️ Flight Fare Prediction")

# Dropdown options
airl = [
    'IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
    'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
    'Vistara Premium economy', 'Jet Airways Business',
    'Multiple carriers Premium economy'
]
sources = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
destinations = ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
stops_list = [0, 1, 2, 3, 4]
months = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
    "June": 6, "July": 7, "August": 8, "September": 9,
    "October": 10, "November": 11, "December": 12
}

# UI Layout
col1, col2, col3, col4 = st.columns(4)
with col1:
    Airline = st.selectbox("Select Airline:", sorted(airl))
with col2:
    source = st.selectbox("Select Source:", sorted(sources))
with col3:
    Dest = st.selectbox("Select Destination:", sorted(destinations))
with col4:
    stops = st.selectbox("Select Stops:", sorted(stops_list))

col5, col6 = st.columns(2)
with col5:
    date = st.selectbox("Select Journey Date:", np.arange(1, 32))
with col6:
    month = st.selectbox("Select Journey Month:", list(months.keys()))

col7, col8, col9 = st.columns(3)
with col7:
    dept_time1 = st.slider("Select Departure Hour", 0, 23, 0)
    dept_time2 = st.slider("Select Departure Minute", 0, 59, 0)
with col8:
    arrival_time1 = st.slider("Select Arrival Hour", 0, 23, 0)
    arrival_time2 = st.slider("Select Arrival Minute", 0, 59, 0)

# Calculate total time
if arrival_time1 > dept_time1 or (arrival_time1 == dept_time1 and arrival_time2 >= dept_time2):
    total_time = (arrival_time1 * 60 + arrival_time2) - (dept_time1 * 60 + dept_time2)
else:
    total_time = (24 * 60 - (dept_time1 * 60 + dept_time2)) + (arrival_time1 * 60 + arrival_time2)

# Prediction button
if st.button("Predict Fare"):
    input_df = pd.DataFrame({
        "Airline": [Airline],
        "Source": [source],
        "Destination": [Dest],
        "Total_Stops": [stops],
        "Dminutes": [abs(total_time)],
        "Journey_date": [date],
        "Journey_month": [months[month]],
        "deph": [dept_time1],
        "depm": [dept_time2],
        "Arrivalh": [arrival_time1],
        "Arrivalm": [arrival_time2]
    })

    result = data.predict(input_df)[0]
    st.success(f"💰 Predicted Fare: {round(result)} Rs")
