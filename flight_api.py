import modal
from modal import App, Image, fastapi_endpoint
from typing import Dict
import pandas as pd
import pickle
from datetime import time

# Define the Docker image to be used
image = Image.debian_slim().pip_install("scikit-learn", "pandas")

# Create a Modal Stub
app = App(name="flight-fare-prediction", image=image)

app = modal.App.lookup('my-app', create_if_missing=True)


sb = modal.Sandbox.create(
    app=app,
    image=modal.Image.debian_slim().add_local_file(
        local_path="C:/Users/HPW/OneDrive/Documents/flyingproject/main.pkl",
        remote_path="/root/main.pkl"
    )
)

@app.function()
@fastapi_endpoint(label="fare-predict", method="POST")
def predict_fare(info: Dict):
    
    # Load the trained model
    main = sb.open("main.pkl", "rb")
    
    # Define valid options
    airline_options = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 'Multiple carriers', 
                       'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy', 
                       'Jet Airways Business', 'Multiple carriers Premium economy']
    source_options = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
    destination_options = ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    
    # Validate input
    error_message = None
    if info["Airline"] not in airline_options:
        error_message = f"Invalid airline. Please select from: {', '.join(airline_options)}"
    if info["Source"] not in source_options:
        error_message = f"Invalid source. Please select from: {', '.join(source_options)}"
    if info["Destination"] not in destination_options:
        error_message = f"Invalid destination. Please select from: {', '.join(destination_options)}"
    if error_message:
        return {"error": error_message}
    
    # Calculate total travel time in minutes
    departure_time = time(info["Departure_hour"], info["Departure_minute"])
    arrival_time = time(info["Arrival_hour"], info["Arrival_minute"])
    if arrival_time > departure_time:
        total_time = (arrival_time.hour * 60 + arrival_time.minute) - (departure_time.hour * 60 + departure_time.minute)
    else:
        total_time = (24 * 60 - (departure_time.hour * 60 + departure_time.minute)) + (arrival_time.hour * 60 + arrival_time.minute)
    
    
    # Create a DataFrame for the model input
    input_df = pd.DataFrame({
        "Airline": [info["Airline"]],
        "Source": [info["Source"]],
        "Destination": [info["Destination"]],
        "Total_Stops": [info["Total_Stops"]],
        "Dminutes": [abs(total_time)],
        "Journey_date": [info["Journey_date"]],
        "Journey_month": [months[info["Journey_month"]]],
        "deph": [info["Departure_hour"]],
        "depm": [info["Departure_minute"]],
        "Arrivalh": [info["Arrival_hour"]],
        "Arrivalm": [info["Arrival_minute"]],
    })
    
    # Predict the fare
    result = main.predict(input_df)[0]
    return {"predicted_fare (Rs) ": round(result)}
