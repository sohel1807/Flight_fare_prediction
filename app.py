import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time
import pickle
import sklearn
data=pickle.load(open("main.pkl","rb"))
st.title("Flight Fare Prediction")
airl=['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy']
source=['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
destination=['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
stops=[0,1,2,3,4]
months = {"January": 1,
           "February": 2,
           "March": 3, 
           "April": 4, 
           "May": 5,
           "June": 6,
           "July": 7,
           "August": 8,
           "September": 9,
           "October": 10,
           "November": 11,
           "December": 12
          }
total_time=0
col1,col2,col3,col4 =st.columns(4)
with col1:
    Airline=st.selectbox("Select Airline:",sorted(airl))
with col2:
    source=st.selectbox("Select source:",sorted(source))
with col3:
    Dest=st.selectbox("Select Destination:",sorted(destination))
with col4:
    stops=st.selectbox("Select stops:",sorted(stops))
col5,col6 =st.columns(2)
with col5:
    date=st.selectbox("Select Journey date:",np.arange(1,32))
with col6:
    month=st.selectbox("Select journey month:",list(months.keys()))
col7,col8,col9,col10= st.columns(4)
with col7:
    dept_time1 = st.slider("Select Departure hour", 0, 23, 0)
with col7:
    dept_time2 = st.slider("Select Departure Minute", 0, 59, 0)
with col9:
    arrival_time1=st.slider("Select Arrival hour", 0, 23, 0)
    arrival_time2=st.slider("Select Arrival minute", 0, 59, 0)
Departure_time = time(dept_time1, dept_time2)
Arrival_time = time(arrival_time1, arrival_time2)
if arrival_time1 > dept_time1 or (arrival_time1 == dept_time1 and arrival_time2 >= dept_time2):
    total_time = (arrival_time1 * 60 + arrival_time2) - (dept_time1 * 60 + dept_time2)
else:
    total_time = (24 * 60 - (dept_time1 * 60 + dept_time2)) + (arrival_time1 * 60 + arrival_time2)
if st.button("Predict Fare"):
    input_df=pd.DataFrame({"Airline":[Airline],"Source":[source],"Destination":[Dest],
                           "Total_Stops":[stops],"Dminutes":[abs(total_time)],"Journey_date":[date],"Journey_month":[months[month]],
                           "deph":[dept_time1],"depm":[dept_time2],"Arrivalh":[arrival_time1],"Arrivalm":[arrival_time2]})
    result=data.predict(input_df)[0]
    st.title(f"Predicted Fare :{round(result)} RS")
