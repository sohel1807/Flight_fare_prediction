from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("main.pkl", "rb"))

# Flask app
app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Months mapping
months = {
    "January": 1, "February": 2, "March": 3,
    "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9,
    "October": 10, "November": 11, "December": 12
}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        Airline = data["Airline"]
        Source = data["Source"]
        Destination = data["Destination"]
        Total_Stops = int(data["Total_Stops"])
        Journey_date = int(data["Journey_date"])
        Journey_month = months[data["Journey_month"]]
        deph = int(data["deph"])
        depm = int(data["depm"])
        Arrivalh = int(data["Arrivalh"])
        Arrivalm = int(data["Arrivalm"])

        # Calculate total duration in minutes
        if Arrivalh > deph or (Arrivalh == deph and Arrivalm >= depm):
            total_time = (Arrivalh * 60 + Arrivalm) - (deph * 60 + depm)
        else:
            total_time = (24 * 60 - (deph * 60 + depm)) + (Arrivalh * 60 + Arrivalm)

        # Create input dataframe
        input_df = pd.DataFrame({
            "Airline": [Airline],
            "Source": [Source],
            "Destination": [Destination],
            "Total_Stops": [Total_Stops],
            "Dminutes": [abs(total_time)],
            "Journey_date": [Journey_date],
            "Journey_month": [Journey_month],
            "deph": [deph],
            "depm": [depm],
            "Arrivalh": [Arrivalh],
            "Arrivalm": [Arrivalm]
        })

        # Predict
        prediction = model.predict(input_df)[0]

        return jsonify({"Predicted Fare (Rs)": round(float(prediction), 2)})

    except Exception as e:
        return jsonify({"error": str(e)})
