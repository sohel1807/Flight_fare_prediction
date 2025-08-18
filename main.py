from fastapi import FastAPI, Request
from pydantic import BaseModel
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("main.pkl", "rb"))

# Define months mapping
months = {
    "January": 1, "February": 2, "March": 3,
    "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9,
    "October": 10, "November": 11, "December": 12
}

# Create FastAPI app
app = FastAPI(title="Flight Fare Prediction API")

# Input schema using Pydantic
class FlightInput(BaseModel):
    Airline: str
    Source: str
    Destination: str
    Total_Stops: int
    Journey_date: int
    Journey_month: str
    deph: int
    depm: int
    Arrivalh: int
    Arrivalm: int

@app.get("/")
def home():
    return {"message": "Flight Fare Prediction API is running!"}

@app.post("/predict")
def predict_fare(data: FlightInput):
    try:
        # Convert month string to int
        Journey_month = months[data.Journey_month]

        # Calculate total duration in minutes
        if data.Arrivalh > data.deph or (data.Arrivalh == data.deph and data.Arrivalm >= data.depm):
            total_time = (data.Arrivalh * 60 + data.Arrivalm) - (data.deph * 60 + data.depm)
        else:
            total_time = (24 * 60 - (data.deph * 60 + data.depm)) + (data.Arrivalh * 60 + data.Arrivalm)

        # Create input DataFrame
        input_df = pd.DataFrame({
            "Airline": [data.Airline],
            "Source": [data.Source],
            "Destination": [data.Destination],
            "Total_Stops": [data.Total_Stops],
            "Dminutes": [abs(total_time)],
            "Journey_date": [data.Journey_date],
            "Journey_month": [Journey_month],
            "deph": [data.deph],
            "depm": [data.depm],
            "Arrivalh": [data.Arrivalh],
            "Arrivalm": [data.Arrivalm]
        })

        # Predict
        prediction = model.predict(input_df)[0]

        return {"Predicted Fare (Rs)": round(float(prediction), 2)}

    except Exception as e:
        return {"error": str(e)}
