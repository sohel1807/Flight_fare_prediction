# Flight Fare Prediction Web App

## Overview
The Flight Fare Prediction Web App combines data analytics, machine learning, and user-centric design to help travelers find the best deals on flights by predicting fare changes.

## API Usage

### Endpoint
**URL:** `https://sohel1807--fare-predict.modal.run`  
**Method:** `POST`  
**Content-Type:** `application/json`

### Input Parameters
- **Airline**: The airline operating the flight.
- **Source**: The departure city.
- **Destination**: The arrival city.
- **Total_Stops**: The number of stops in the flight.
- **Journey_date**: The date of travel.
- **Journey_month**: The month of travel.
- **Departure_hour**: The hour of departure.
- **Departure_minute**: The minute of departure.
- **Arrival_hour**: The hour of arrival.
- **Arrival_minute**: The minute of arrival.

### Sample Input
```json
{
   "Airline": "IndiGo",
   "Source": "Delhi",
   "Destination": "Banglore",
   "Total_Stops": 1,
   "Journey_date": 15,
   "Journey_month": "March",
   "Departure_hour": 10,
   "Departure_minute": 30,
   "Arrival_hour": 13,
   "Arrival_minute": 45
}
```

### Sample Output
```json
{
   "predicted_fare (Rs)": 4500
}
```

## Software Requirements
1. [VSCode IDE](https://code.visualstudio.com/)
2. [GitHub Account](https://github.com/)
3. [Git CLI](https://git-scm.com/downloads)
4. [Streamlit](https://streamlit.io/cloud)
5. [Data Source](https://www.kaggle.com/)
6. [Docker](https://www.docker.com/)

## Getting Started

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/sohel1807/Flight_fare_prediction.git
```

### 2. Navigate to the Project Directory
```bash
cd Flight_fare_prediction
```

### 3. Install Dependencies
```bash
pip install streamlit
```

### 4. Run the Development Server
Run the project on your local machine:
```bash
streamlit run app.py
```

## Run with Docker

You can easily run the app using the Docker image hosted on Docker Hub:

- **Image:** `sohel1807/flight-fare-prediction`
- **Docker Hub page:** https://hub.docker.com/r/sohel1807/flight-fare-prediction

### Pull and Run the Docker Container

```bash
docker pull sohel1807/flight-fare-prediction
docker run -p 8501:8501 sohel1807/flight-fare-prediction
```

The web application will start running.

## Contributing
If you'd like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome and appreciated!

## Issues
If you encounter any issues or have suggestions for improvement, please open an issue on GitHub, and we'll address it as soon as possible.


